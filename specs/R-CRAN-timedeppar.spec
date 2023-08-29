%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  timedeppar
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Infer Constant and Stochastic, Time-Dependent Model Parameters

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
Infer constant and stochastic, time-dependent parameters to consider
intrinsic stochasticity of a dynamic model and/or to analyze model
structure modifications that could reduce model deficits. The concept is
based on inferring time-dependent parameters as stochastic processes in
the form of Ornstein-Uhlenbeck processes jointly with inferring constant
model parameters and parameters of the Ornstein-Uhlenbeck processes. The
package also contains functions to sample from and calculate densities of
Ornstein-Uhlenbeck processes. References: Tomassini, L., Reichert, P.,
Kuensch, H.-R. Buser, C., Knutti, R. and Borsuk, M.E. (2009), A smoothing
algorithm for estimating stochastic, continuous-time model parameters and
its application to a simple climate model, Journal of the Royal
Statistical Society: Series C (Applied Statistics) 58, 679-704,
<doi:10.1111/j.1467-9876.2009.00678.x> Reichert, P., and Mieleitner, J.
(2009), Analyzing input and structural uncertainty of nonlinear dynamic
models with stochastic, time-dependent parameters. Water Resources
Research, 45, W10402, <doi:10.1029/2009WR007814> Reichert, P., Ammann, L.
and Fenicia, F. (2021), Potential and challenges of investigating
intrinsic uncertainty of hydrological models with time-dependent,
stochastic parameters. Water Resources Research 57(8), e2020WR028311,
<doi:10.1029/2020WR028311> Reichert, P. (2022), timedeppar: An R package
for inferring stochastic, time-dependent model parameters, in preparation.

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
