%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesqm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Q Methodology: Exact Rank-Order Likelihood for Forced Q Sorts

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-posterior >= 1.5.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-clue 
Requires:         R-CRAN-posterior >= 1.5.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-clue 

%description
A Bayesian analysis for Q methodology, alongside the classical one. Models
the forced Q sort as an ordered partition of the statements through an
exact rank-order likelihood (the design quotas fix the partition margins,
so the likelihood of the observed sorting event is exact), fits it by a
parameter-expanded Gibbs sampler in R with no compiled code and a
convergence gate on rotation-invariant functionals, resolves rotational
ambiguity via the MatchAlign post-processing of Poworoznek et al. (2025)
<doi:10.1214/25-BA1544>, and returns the familiar Q tables as posterior
summaries: credible intervals for bounded participant loadings, flag
probabilities with an explicit unclassified state, quota-respecting factor
arrays, distinguishing and consensus statements judged against a posterior
critical difference and a grid-width equivalence region, one posterior
false-discovery rule for all published claims, and a two-signal
posterior-predictive workflow for the number of factors.

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
