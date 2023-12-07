%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcmdrPlugin.DCE
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Plug-in for Discrete Choice Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-support.CEs >= 0.7.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Rcmdr 
Requires:         R-CRAN-support.CEs >= 0.7.0
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Rcmdr 

%description
Adds menu items for discrete choice experiments (DCEs) to the R Commander.
DCE is a question-based survey method that designs various combinations
(profiles) of attribute levels using the experimental designs, asks
respondents to select the most preferred profile in each choice set, and
then measures preferences for the attribute levels by analyzing the
responses. For details on DCEs, refer to Louviere et al. (2000)
<doi:10.1017/CBO9780511753831>.

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
