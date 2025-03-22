%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DPTM
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Panel Multiple Threshold Model with Fixed Effects

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-BayesianTools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-parabar 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-R6 
Requires:         R-CRAN-BayesianTools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-parabar 
Requires:         R-utils 

%description
Compute the fixed effects dynamic panel threshold model suggested by
Ramírez-Rondán (2020) <doi:10.1080/07474938.2019.1624401>, and dynamic
panel linear model suggested by Hsiao et al. (2002)
<doi:10.1016/S0304-4076(01)00143-9>, where maximum likelihood type
estimators are used. Multiple thresholds estimation based on Markov Chain
Monte Carlo (MCMC) is allowed, and model selection of linear model,
threshold model and multiple threshold model is also allowed.

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
