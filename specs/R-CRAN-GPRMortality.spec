%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPRMortality
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Process Regression for Mortality Rates

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-rstantools
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-rstantools

%description
A Bayesian statistical model for estimating child (under-five age group)
and adult (15-60 age group) mortality.  The main challenge is how to
combine and integrate these different time series and how to produce
unified estimates of mortality rates during a specified time span. GPR is
a Bayesian statistical model for estimating child and adult mortality
rates which its data likelihood is mortality rates from different data
sources such as: Death Registration System, Censuses or surveys. There are
also various hyper-parameters for completeness of DRS, mean, covariance
functions and variances as priors. This function produces estimations and
uncertainty (95%% or any desirable percentiles) based on sampling and
non-sampling errors due to variation in data sources. The GP model
utilizes Bayesian inference to update predicted mortality rates as a
posterior in Bayes rule by combining data and a prior probability
distribution over parameters in mean, covariance function, and the
regression model. This package uses Markov Chain Monte Carlo (MCMC) to
sample from posterior probability distribution by 'rstan' package in R.
Details are given in Wang H, Dwyer-Lindgren L, Lofgren KT, et al. (2012)
<doi:10.1016/S0140-6736(12)61719-X>, Wang H, Liddell CA, Coates MM, et al.
(2014) <doi:10.1016/S0140-6736(14)60497-9> and Mohammadi, Parsaeian,
Mehdipour et al. (2017) <doi:10.1016/S2214-109X(17)30105-5>.

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
