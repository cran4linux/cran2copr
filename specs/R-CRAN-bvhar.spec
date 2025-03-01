%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bvhar
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Vector Heterogeneous Autoregressive Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-BH >= 1.87.0.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.4.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.0
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-RcppSpdlog 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-Rcpp >= 0.10.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-optimParallel 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-bayesplot 

%description
Tools to model and forecast multivariate time series including Bayesian
Vector heterogeneous autoregressive (VHAR) model by Kim & Baek (2023)
(<doi:10.1080/00949655.2023.2281644>). 'bvhar' can model Vector
Autoregressive (VAR), VHAR, Bayesian VAR (BVAR), and Bayesian VHAR (BVHAR)
models.

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
