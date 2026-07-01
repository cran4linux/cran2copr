%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  uddbart
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Dynamic Deep 'BART' for Interval-Censored Survival

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Implements U-DDBART-IC, a unified Bayesian workflow for dynamic risk
prediction from irregular longitudinal biomarkers when event times are
interval-censored between clinical visits. The package turns long-format
biomarker histories and patient-level interval endpoints L, R, C and delta
into a discrete-time follow-up grid, summarises each landmark history with
nine interpretable trajectory features (current, baseline and previous
biomarker values, last visit gap, local slope, cumulative decline, best
value, elapsed time and visit count), fits discrete-time interval hazards
using optional logit-link Bayesian additive regression trees, a
generalized linear model fallback, or a lightweight variational
approximation, accumulates survival from the discrete-time product, and
evaluates the interval-censored likelihood. Fitted models return landmark
risk predictions over user-specified horizons with posterior or bootstrap
uncertainty by evaluating survival ratios across fitted hazard draws.
Utilities are provided for simulation, staged model fitting, plotting and
summarising dynamic risk curves, IPCW Brier scores, cumulative/dynamic
time-dependent area under the curve, calibration tables, and an anonymised
chronic myeloid leukaemia molecular-monitoring example data set.

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
