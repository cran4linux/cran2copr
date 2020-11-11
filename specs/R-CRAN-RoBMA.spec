%global packname  RoBMA
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Bayesian Meta-Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    jags-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-DPQ 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-bridgesampling 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-psych 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-DPQ 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-Rdpack 

%description
A framework for estimating ensembles of meta-analytic models (assuming
either presence or absence of the effect, heterogeneity, and publication
bias) and using Bayesian model averaging to combine them. The ensembles
use Bayes factors to test for the presence or absence of the individual
components (e.g., effect vs. no effect) and model-averages parameter
estimates based on posterior model probabilities (Maier, Bartoš &
Wagenmakers, 2020, <doi:10.31234/osf.io/u4cns>). The user can define a
wide range of non-informative or informative priors for the effect size,
heterogeneity, and weight functions. The package provides convenient
functions for summary, visualizations, and fit diagnostics.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
