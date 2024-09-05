%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SVDNF
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Nonlinear Filtering for Stochastic Volatility Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 

%description
Implements the discrete nonlinear filter (DNF) of Kitagawa (1987)
<doi:10.1080/01621459.1987.10478534> to a wide class of stochastic
volatility (SV) models with return and volatility jumps following the work
of Bégin and Boudreault (2021) <doi:10.1080/10618600.2020.1840995>. Offers
several built-in SV models and a flexible framework for users to create
customized models by specifying drift and diffusion functions along with a
jump arrival distribution for the return and volatility dynamics. Allows
for the estimation of factor models with stochastic volatility (e.g.,
heteroskedastic volatility CAPM) by incorporating expected return
predictors. `Includes functions to compute likelihood evaluations,
filtering and prediction distribution estimates, maximum likelihood
parameter estimates, to simulate data from built-in and custom SV models
with jumps, and to forecast future returns and volatility values using
Monte Carlo simulation from a given SV model.

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
