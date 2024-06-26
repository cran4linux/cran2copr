%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CausalGPS
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Matching on Generalized Propensity Scores with Continuous Exposures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-wCorr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-gnm 
BuildRequires:    R-CRAN-locpol 
BuildRequires:    R-CRAN-Ecume 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-parallel 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-wCorr 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-gnm 
Requires:         R-CRAN-locpol 
Requires:         R-CRAN-Ecume 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-cowplot 

%description
Provides a framework for estimating causal effects of a continuous
exposure using observational data, and implementing matching and weighting
on the generalized propensity score. Wu, X., Mealli, F., Kioumourtzoglou,
M.A., Dominici, F. and Braun, D., 2022. Matching on generalized propensity
scores with continuous exposures. Journal of the American Statistical
Association, pp.1-29.

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
