%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RoBMA
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Bayesian Meta-Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    jags-devel
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-BayesTools >= 0.2.0
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-bridgesampling 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-BayesTools >= 0.2.0
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-bridgesampling 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-psych 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 

%description
A framework for estimating ensembles of meta-analytic models (assuming
either presence or absence of the effect, heterogeneity, and publication
bias). The RoBMA framework uses Bayesian model-averaging to combine the
competing meta-analytic models into a model ensemble, weights the
posterior parameter distributions based on posterior model probabilities
and uses Bayes factors to test for the presence or absence of the
individual components (e.g., effect vs. no effect; Bartoš et al., 2021,
<doi:10.31234/osf.io/kvsp7>; Maier, Bartoš & Wagenmakers, in press,
<doi:10.31234/osf.io/u4cns>). Users can define a wide range of
non-informative or informative prior distributions for the effect size,
heterogeneity, and publication bias components (including selection models
and PET-PEESE). The package provides convenient functions for summary,
visualizations, and fit diagnostics.

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
find -type f -exec sed -i 's/-llapack/-lflexiblas/g' {} \;

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
