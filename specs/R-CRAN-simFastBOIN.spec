%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simFastBOIN
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Simulation of Bayesian Optimal Interval Designs for Phase I and Phase I/II Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-Iso 
Requires:         R-stats 
Requires:         R-utils 

%description
Design and evaluate phase I dose-finding trials that use the Bayesian
optimal interval (BOIN) design of Liu and Yuan (2015)
<doi:10.1111/rssc.12089>. Functions are provided to tabulate the decision
boundaries, to simulate trials, to estimate the dose-toxicity curve under
a monotonicity constraint and to select the maximum tolerated dose. The
simulation engine is written in C++ and draws one random variate per
patient in enrollment order, which reproduces the reference implementation
in the 'BOIN' package trial by trial for a given seed. The traditional 3+3
design is provided as a comparator, with operating characteristics
obtained in closed form rather than by simulation. For toxicity that is
observed late, the time-to-event BOIN design is provided with the two
estimators of Yuan and colleagues (2018)
<doi:10.1158/1078-0432.CCR-18-0246> and Lin and Yuan (2020)
<doi:10.1093/biostatistics/kxz007>. Patients who arrive while the dose
escalation waits can be backfilled to lower doses with the designs of Zhao
and colleagues (2024) <doi:10.1158/1078-0432.CCR-23-2585> and Chen and
colleagues (2026) <doi:10.1007/s43441-026-00994-0>, the latter with the
suspension rules of Chen and colleagues (2025)
<doi:10.1158/1078-0432.CCR-24-3669>. Trials of two drugs given together
are handled by the drug-combination design of Lin and Yin (2017)
<doi:10.1177/0962280215594494>. The optimal biological dose, which weighs
the response against the toxicity, is found with the BOIN-ET design of
Takeda and colleagues (2018) <doi:10.1002/pst.1864>, with the estimators
and selection rules of the 'boinet' package, its time-to-event version
(Takeda and colleagues, 2020) <doi:10.1002/pst.1995> and its backfill
version (Takeda and colleagues, 2025) <doi:10.1002/pst.2470>, and with the
BOIN12 design of Lin and colleagues (2020) <doi:10.1200/PO.20.00257>,
which weighs them by a utility, and its time-to-event version (Zhou and
colleagues, 2022) <doi:10.1002/sim.9337>. For two drugs given together,
the optimal dose combination is found with the Comb-BOIN12 design of Lu
and colleagues (2025) <doi:10.1080/19466315.2024.2370403>, also in its
time-to-event version, and the BOIN-ETC design of Kakizume and colleagues
(2024) <doi:10.1177/09622802241236936>. The titration of the BOIN design
can be limited to the lowest doses, as in the accelerated design of Kojima
and colleagues (2024) <doi:10.1007/s43441-024-00692-9>. The operating
characteristics of several designs can be tabulated and plotted side by
side.

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
