%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AHTauDesign
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Truncation Time Selection for Average Hazard Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements a two-stage, design-informed framework for selecting the
truncation time in time-to-event trials analyzed with the average hazard
estimand, motivated by pediatric oncology settings with small samples,
slow accrual, and limited follow-up. Stage 1 validates a clinically
proposed truncation time against the planned design using simulation-based
diagnostics for risk-set support, follow-up coverage, estimability, and
estimator stability, classifying it as Pass, Borderline, or Fail. Stage 2
performs constrained optimization over a grid of candidate truncation
times within a clinical-distance window, maximizing a utility subject to
feasibility constraints, with an independent evaluation run to assess the
selected time. Supports proportional-hazards, early-, and delayed-effect
patterns, uniform accrual with administrative censoring, and calibrated
exponential random censoring.

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
