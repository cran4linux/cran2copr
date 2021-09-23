%global __brp_check_rpaths %{nil}
%global packname  cAIC4
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Akaike Information Criterion for 'lme4' and 'nlme'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.1.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-lme4 >= 1.1.6
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-stats4 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-RLRsim 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-mvtnorm 

%description
Provides functions for the estimation of the conditional Akaike
information in generalized mixed-effect models fitted with (g)lmer() from
'lme4', lme() from 'nlme' and gamm() from 'mgcv'. For a manual on how to
use 'cAIC4', see Saefken et al. (2021) <doi:10.18637/jss.v099.i08>.

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
