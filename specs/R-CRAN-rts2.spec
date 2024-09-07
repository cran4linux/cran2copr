%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rts2
%global packver   0.7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.6
Release:          1%{?dist}%{?buildtag}
Summary:          Real-Time Disease Surveillance

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-StanHeaders >= 2.32.0
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-sf >= 1.0.14
BuildRequires:    R-CRAN-glmmrBase >= 0.7.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-SparseChol >= 0.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-sf >= 1.0.14
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rstantools

%description
Supports modelling real-time case data to facilitate the real-time
surveillance of infectious diseases and other point phenomena. The package
provides automated computational grid generation over an area of interest
with methods to map covariates between geographies, model fitting
including spatially aggregated case counts, and predictions and
visualisation. Both Bayesian and maximum likelihood methods are provided.
Log-Gaussian Cox Processes are described by Diggle et al. (2013)
<doi:10.1214/13-STS441> and we provide both the low-rank approximation for
Gaussian processes described by Solin and Särkkä (2020)
<doi:10.1007/s11222-019-09886-w> and Riutort-Mayol et al (2023)
<doi:10.1007/s11222-022-10167-2> and the nearest neighbour Gaussian
process described by Datta et al (2016)
<doi:10.1080/01621459.2015.1044091>. 'cmdstanr' can be downloaded at
<https://mc-stan.org/cmdstanr/>.

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
