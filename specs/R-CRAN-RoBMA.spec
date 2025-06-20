%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RoBMA
%global packver   3.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Bayesian Meta-Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    jags-devel
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-BayesTools >= 0.2.19
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-BayesTools >= 0.2.19
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-rjags 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ggplot2 

%description
A framework for estimating ensembles of meta-analytic, meta-regression,
and multilevel models (assuming either presence or absence of the effect,
heterogeneity, publication bias, and moderators). The RoBMA framework uses
Bayesian model-averaging to combine the competing meta-analytic models
into a model ensemble, weights the posterior parameter distributions based
on posterior model probabilities and uses Bayes factors to test for the
presence or absence of the individual components (e.g., effect vs. no
effect; Bartoš et al., 2022, <doi:10.1002/jrsm.1594>; Maier, Bartoš &
Wagenmakers, 2022, <doi:10.1037/met0000405>; Bartoš et al., 2025,
<doi:10.1037/met0000737>). Users can define a wide range of prior
distributions for the effect size, heterogeneity, publication bias
(including selection models and PET-PEESE), and moderator components. The
package provides convenient functions for summary, visualizations, and fit
diagnostics.

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
