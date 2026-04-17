%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DecisionDrift
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Detecting, Decomposing, and Stress-Testing Temporal Change in Repeated Decision Systems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-stats 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-stats 

%description
Tools for detecting, decomposing, and stress-testing temporal drift in
repeated binary decision systems. Complements the 'decisionpaths' package
by shifting focus from path construction to system-level change over time.
Implements five core analytic modules: (1) prevalence drift — did the
overall decision rate change over time?; (2) transition drift — did the
probability of switching or persisting change?; (3) entropy and stability
trends — did path complexity evolve?; (4) group-differential drift — did
the system drift differently across subgroups?; (5) change-point and
regime-shift detection — did the system change abruptly after a policy or
model update? Additionally provides a robustness module for testing
stability of drift conclusions across analytic choices, and a sensitivity
module for probing vulnerability to data problems including missingness,
miscoding, and threshold shifts. Defines four original drift indices: the
Decision Drift Index (DDI), Transition Drift Index (TDI), Group
Differential Drift (GDD), and Cumulative Drift Burden (CDB). Applications
include algorithmic audit, AI governance, education, health, and
organisational research.

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
