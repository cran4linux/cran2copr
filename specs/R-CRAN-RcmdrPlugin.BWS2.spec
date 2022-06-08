%global __brp_check_rpaths %{nil}
%global packname  RcmdrPlugin.BWS2
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Plug-in for Case 2 Best-Worst Scaling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-support.BWS2 >= 0.4.0
BuildRequires:    R-CRAN-support.CEs 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Rcmdr 
BuildRequires:    R-CRAN-DoE.base 
Requires:         R-CRAN-support.BWS2 >= 0.4.0
Requires:         R-CRAN-support.CEs 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Rcmdr 
Requires:         R-CRAN-DoE.base 

%description
Adds menu items for Case 2 (profile case) best-worst scaling (BWS2) to the
R Commander. BWS2 is a question-based survey method that constructs
profiles (combinations of attribute levels) using an orthogonal array,
asks respondents to select the best and worst levels in each profile, and
measures preferences for attribute levels by analyzing the responses. For
details, see Aizaki and Fogarty (2019) <doi:10.1016/j.jocm.2019.100171>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
