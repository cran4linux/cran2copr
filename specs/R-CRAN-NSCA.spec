%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NSCA
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Necessary and Sufficient Condition Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-NCA >= 5.0.2
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-SCAtools >= 0.4.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-NCA >= 5.0.2
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-SCAtools >= 0.4.1
Requires:         R-stats 
Requires:         R-utils 

%description
Tests and quantifies bivariate statements in which a condition is both
necessary and sufficient for an outcome. Necessity and sufficiency are
estimated as two empty-space frontiers on diagonally opposite corners of
the same scatter plot, using the 'NCA' package of Dul (2016)
<doi:10.1177/1094428115584005> for the necessity side and 'SCAtools' for
the sufficiency side. The two empty zones and the region between them tile
the analytic scope, which yields the reported areas as one identity rather
than as separate definitions: a weakest-component effect, a normalised
geometric mean of the two components, the share of the scope the claims
jointly rule out, and the data zone they still admit. The conjunction is
decided by an intersection-union combination of the two directional
permutation tests, optionally driven by a single shared permutation
sequence so that a statistic of both components can also be tested. These
are random-pairing screens rather than direct tests of a causal
necessary-and-sufficient relation, no magnitude benchmarks are asserted
for the joint indices, and a dual-threshold table separates outcome levels
that are out of reach, admitted, or guaranteed. An ordinary least-squares
line can be drawn alongside the two frontiers as a central-tendency
reference; it is an average-effect summary and is never treated as a
component of either claim.

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
