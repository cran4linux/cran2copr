%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LatencyA
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Latency Analysis in Epidemiological Studies Using Weighted Cumulative Exposures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 

%description
Implements weighted cumulative exposure Cox proportional hazards models
for latency analysis with repeatedly measured, time-varying exposures.
Instead of entering every lagged exposure as a separate and highly
correlated covariate, the lag-specific log hazard ratios are constrained
to follow a smooth function of the time since exposure, parameterized by
natural cubic splines or polynomials, so that the susceptible window of an
exposure can be identified from the estimated lag-risk curve. Functions
are provided to fit models with a prespecified number of knots or
polynomial degree, to select the number of knots by a grid search or the
spline terms by a stepwise search using the Akaike or Bayesian information
criterion, and to extract lag-specific log hazard ratios with their
variances. For the data-driven model selection procedures, inference is
based on a cluster bootstrap that resamples subjects, which can be run
sequentially or in parallel. The methods are described in Guo, Qian, Wang,
Wang, Rosner and Wang (2026) "Taking Into Account the Susceptible Window
for Exposures in Cox Proportional Hazards Model: A Way Using Splines to
Model the Lag-Risk Relationship" <doi:10.1002/sim.70755>.

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
