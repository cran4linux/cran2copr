%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsge
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Stochastic General Equilibrium Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 

%description
Specify, solve, and estimate dynamic stochastic general equilibrium (DSGE)
models by maximum likelihood and Bayesian methods. Supports both linear
models via an equation-based formula interface and nonlinear models via
string-based equations with first-order perturbation (linearization around
deterministic steady state). Solution uses the method of undetermined
coefficients (Klein, 2000 <doi:10.1016/S0165-1889(99)00045-7>). Likelihood
evaluated via the Kalman filter. Bayesian estimation uses adaptive
Random-Walk Metropolis-Hastings with prior specification. Additional tools
include Kalman smoothing, historical shock decomposition, local
identification diagnostics, parameter sensitivity analysis, second-order
perturbation, occasionally binding constraints, impulse-response
functions, forecasting, and robust standard errors.

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
