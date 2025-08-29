%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesianMCPMod
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate, Evaluate, and Analyze Dose Finding Trials with Bayesian MCPMod

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-DoseFinding >= 1.1.1
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-RBesT 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-DoseFinding >= 1.1.1
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-RBesT 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Bayesian MCPMod (Fleischer et al. (2022) <doi:10.1002/pst.2193>) is an
innovative method that improves the traditional MCPMod by systematically
incorporating historical data, such as previous placebo group data. This R
package offers functions for simulating, analyzing, and evaluating
Bayesian MCPMod trials with normally distributed endpoints.  It enables
the assessment of trial designs incorporating historical data across
various true dose-response relationships and sample sizes. Robust mixture
prior distributions, such as those derived with the
Meta-Analytic-Predictive approach (Schmidli et al. (2014)
<doi:10.1111/biom.12242>), can be specified for each dose group.
Resulting mixture posterior distributions are used in the Bayesian
Multiple Comparison Procedure and modeling steps. The modeling step also
includes a weighted model averaging approach (Pinheiro et al. (2014)
<doi:10.1002/sim.6052>). Estimated dose-response relationships can be
bootstrapped and visualized.

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
