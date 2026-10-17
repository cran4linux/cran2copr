%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DecisionDrift
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
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
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for detecting, decomposing, and testing temporal change in repeated
binary decision systems. Decomposes each change in the decision rate into
inflow (uptake) and outflow (reversal) through the marginal-transition
identity, separates net change from gross turnover, and splits aggregate
change into within-group and composition components with a symmetric
midpoint decomposition. A unit-level cluster bootstrap gives intervals for
every component and a global test of process stability with
family-wise-adjusted contrasts and simultaneous confidence bands. Also
provides prevalence and transition drift summaries, entropy trends,
group-differential drift, change-point diagnostics, robustness and
sensitivity analyses, an integrated audit, and a simulator for stable,
marginal, masked, abrupt, group-masked, and composition-change scenarios.
Complements the 'decisionpaths' package. Applications include algorithmic
audit, AI governance, education, health, and organisational research.

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
