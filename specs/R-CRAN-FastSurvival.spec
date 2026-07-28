%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FastSurvival
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Survival Analysis and Simulation for Clinical Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-dqrng 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-mvtnorm 

%description
Provides fast alternatives to standard survival analysis functions in the
'survival' package, together with tools for time-to-event trial simulation
and sequential analysis. The estimation and testing functions cover a
single-time-point Kaplan-Meier estimator (survfit_fast()), log-rank tests
including weighted and stratified variants (survdiff_fast()), a
closed-form hazard ratio estimator based on the Pike-Halley Estimator
method (coxph_fast()), restricted mean survival time (rmst_fast()), window
mean survival time (wmst_fast()), milestone survival comparison
(milestone_fast()), median survival time (medsurv_fast()), the max-combo
test (maxcombo_fast()), the robust modestly-weighted log-rank test
(rmw_fast()), the weighted Kaplan-Meier (Pepe-Fleming) test (wkm_fast()),
the average hazard with survival weight (ahsw_fast()), and the
Kalbfleisch-Prentice average hazard ratio (ahr_fast()). The simulation
layer generates individual patient data (simdata_fast()), performs interim
or sequential analyses (analysis_fast()), and aggregates operating
characteristics (simsummary_fast()). A visualization layer assembles
design-stage scenarios (gen_scenario_fast()) and builds analysis-stage
Kaplan-Meier curves (kmcurve_fast()), each with plot and print methods.
All functions are designed for repeated evaluation inside large simulation
loops, such as adaptive sample-size re-estimation, probability-of-success
calculations, and regional consistency evaluation in multi-regional
trials. Core computations are implemented in 'C++' via 'Rcpp' for maximum
performance. Methodological background is described in Collett (2014,
ISBN:9780429196294).

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
