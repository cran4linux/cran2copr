%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpiNova
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Extended State-Space Epidemiological Models with Modern Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-splines 
Requires:         R-CRAN-scales 

%description
An extended epidemiological modelling framework that goes beyond the
classical SIR (Susceptible-Infectious-Recovered) model. Supports SEIR
(Susceptible-Exposed-Infectious-Recovered), SEIRD
(Susceptible-Exposed-Infectious-Recovered-Deceased), SVEIRD
(Susceptible-Vaccinated-Exposed-Infectious-Recovered-Deceased), and
age-stratified compartmental models with flexible intervention functions
(spline-based, Gaussian process, or user-defined). Inference is available
via maximum likelihood or sequential Monte Carlo (SMC, also known as
particle filtering) with no external binary dependencies. Includes a
dependency-free real-time effective reproduction number (Rt) estimator,
spatial multi-patch models with gravity-model mobility, ensemble
forecasting via Bayesian model averaging (BMA), and proper scoring rules
including CRPS (Continuous Ranked Probability Score), coverage, and MAE
(Mean Absolute Error) for forecast evaluation. Methods follow Anderson and
May (1991, ISBN:9780198545996), Doucet, de Freitas, and Gordon (2001)
<doi:10.1007/978-1-4757-3437-9>, Cori et al. (2013)
<doi:10.1093/aje/kwt133>, and Gneiting and Raftery (2007)
<doi:10.1198/016214506000001437>.

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
