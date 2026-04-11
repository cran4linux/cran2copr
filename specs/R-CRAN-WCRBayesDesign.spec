%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WCRBayesDesign
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Two-Stage Design with Window-Cohort and Controlled Roll-on for Time-to-Event Estimand

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-stats 
Requires:         R-parallel 

%description
Calibrates Bayesian two-stage designs for single-arm phase II trials with
time-to-event endpoints using a window-cohort with controlled roll-on.
Interim monitoring is anchored to a locked interim cohort and a
pre-specified follow-up requirement, so analysis timing remains
predictable while preserving follow-up maturity. The package searches
feasible interim rules, optimizes final sample size and decision
thresholds, evaluates operating characteristics by Monte Carlo simulation,
and supports exponential, Weibull, log-normal, log-logistic, and
user-defined baseline survival models. Related published foundations
include Simon (1989) <doi:10.1016/0197-2456(89)90015-9> and Cotterill and
Whitehead (2015) <doi:10.1002/sim.6426>.

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
