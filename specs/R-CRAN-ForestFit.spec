%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ForestFit
%global packver   2.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Modelling for Plant Size Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.4
Requires:         R-core >= 3.4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ars 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-ars 
Requires:         R-CRAN-pracma 

%description
Developed for the following tasks. 1 ) Computing the probability density
function, cumulative distribution function, random generation, and
estimating the parameters of the eleven mixture models. 2 ) Point
estimation of the parameters of two - parameter Weibull distribution using
twelve methods and three - parameter Weibull distribution using nine
methods. 3 ) The Bayesian inference for the three - parameter Weibull
distribution. 4 ) Estimating parameters of the three - parameter Birnbaum
- Saunders, generalized exponential, and Weibull distributions fitted to
grouped data using three methods including approximated maximum
likelihood, expectation maximization, and maximum likelihood. 5 )
Estimating the parameters of the gamma, log-normal, and Weibull mixture
models fitted to the grouped data through the EM algorithm, 6 ) Estimating
parameters of the nonlinear height curve fitted to the height - diameter
observation, 7 ) Estimating parameters, computing probability density
function, cumulative distribution function, and generating realizations
from gamma shape mixture model introduced by Venturini et al. (2008)
<doi:10.1214/07-AOAS156> , 8 ) The Bayesian inference, computing
probability density function, cumulative distribution function, and
generating realizations from univariate and bivariate Johnson SB
distribution, 9 ) Robust multiple linear regression analysis when error
term follows skewed t distribution, 10 ) Estimating parameters of a given
distribution fitted to grouped data using method of maximum likelihood,
and 11 ) Estimating parameters of the Johnson SB distribution through the
Bayesian, method of moment, conditional maximum likelihood, and two -
percentile method.

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
