%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsge
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
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
string-based equations with perturbation up to third order (Schmitt-Grohe
and Uribe, 2004 <doi:10.1016/S0165-1889(03)00043-5>). Solution uses the
method of undetermined coefficients (Klein, 2000
<doi:10.1016/S0165-1889(99)00045-7>). Likelihood evaluated via the Kalman
filter or a bootstrap particle filter (Gordon et al., 1993). Bayesian
estimation uses adaptive Random-Walk Metropolis-Hastings or Particle
Marginal Metropolis-Hastings (Andrieu et al., 2010
<doi:10.1111/j.1467-9868.2009.00736.x>) with parallel chain support.
Additional tools include Bayes factor model comparison with Kass-Raftery
evidence scales, Ramsey optimal policy via linear-quadratic regulator,
nonlinear perfect foresight via stacked-time Newton (Juillard et al.,
1998), Kalman smoothing, historical shock decomposition, local
identification diagnostics, parameter sensitivity analysis, occasionally
binding constraints, impulse-response functions, forecasting, and robust
standard errors.

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
