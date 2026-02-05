%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpiNow2
%global packver   1.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate and Forecast Real-Time Infection Dynamics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-rstantools >= 2.2.0
BuildRequires:    R-CRAN-R.utils >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-futile.logger >= 1.4
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-primarycensored 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-runner 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-rstantools >= 2.2.0
Requires:         R-CRAN-R.utils >= 2.0.0
Requires:         R-CRAN-futile.logger >= 1.4
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-primarycensored 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-runner 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-truncnorm 
Requires:         R-utils 
Requires:         R-CRAN-rstantools

%description
Estimates the time-varying reproduction number, rate of spread, and
doubling time using a renewal equation approach combined with Bayesian
inference via Stan. Supports Gaussian process and random walk priors for
modelling changes in transmission over time. Accounts for delays between
infection and observation (incubation period, reporting delays),
right-truncation in recent data, day-of-week effects, and observation
overdispersion. Can estimate relationships between primary and secondary
outcomes (e.g., cases to hospitalisations or deaths) and forecast both.
Runs across multiple regions in parallel. Based on Abbott et al. (2020)
<doi:10.12688/wellcomeopenres.16006.1> and Gostic et al. (2020)
<doi:10.1101/2020.06.18.20134858>.

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
