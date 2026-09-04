%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modMStates
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation and Estimation of Continuous-Time Multi-State Markov Models for Panel Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-msm >= 1.6
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-msm >= 1.6
Requires:         R-stats 
Requires:         R-utils 

%description
A higher-level interface to continuous-time Markov multi-state models for
panel (interval-censored) data. Seven canonical clinical process
structures are supplied with structurally valid generator matrices, so
that transition matrices and starting values need not be constructed by
hand. Panel data can be simulated from exact trajectories under regular or
irregular observation schedules, with optional exactly observed absorption
times and optional Weibull holding times for assessing the Markov
assumption. A single fitting call validates the input against the assumed
structure and returns the estimated generator with confidence intervals,
mean sojourn times, transition probability matrices and observed
transition counts, together with the optimiser's convergence code. A Monte
Carlo driver reports Monte Carlo standard errors alongside bias, root mean
squared error and interval coverage. Likelihood evaluation is delegated to
'msm' (Jackson, 2011, <doi:10.18637/jss.v038.i08>); the panel-data
likelihood is that of Kalbfleisch and Lawless (1985)
<doi:10.1080/01621459.1985.10478195>.

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
