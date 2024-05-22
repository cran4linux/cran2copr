%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcmdrPlugin.BWS3
%global packver   0.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Plug-in for Case 3 Best-Worst Scaling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-support.BWS3 
BuildRequires:    R-CRAN-support.CEs 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Rcmdr 
Requires:         R-CRAN-support.BWS3 
Requires:         R-CRAN-support.CEs 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Rcmdr 

%description
Adds menu items for case 3 (multi-profile) best-worst scaling (BWS3) to
the R Commander. BWS3 is a question-based survey method that designs
various combinations of attribute levels (profiles), asks respondents to
select the best and worst profiles in each choice set, and then measures
preferences for the attribute levels by analyzing the responses. For
details on BWS3, refer to Louviere et al. (2015)
<doi:10.1017/CBO9781107337855>.

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
