%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bartisan
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Bayesian Additive Regression Trees

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 4.0.1
BuildRequires:    R-CRAN-cli >= 3.6.4
BuildRequires:    R-CRAN-rlang >= 1.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.2
BuildRequires:    R-CRAN-reformulas >= 0.4.4
BuildRequires:    R-CRAN-arg >= 0.2.1
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 4.0.1
Requires:         R-CRAN-cli >= 3.6.4
Requires:         R-CRAN-rlang >= 1.2.0
Requires:         R-CRAN-Rcpp >= 1.1.2
Requires:         R-CRAN-reformulas >= 0.4.4
Requires:         R-CRAN-arg >= 0.2.1
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits Bayesian additive regression trees (BART) models for likelihoods
outside the conditionally conjugate Gaussian case, using the
Laplace-approximation reversible-jump sampler of Linero (2025)
<doi:10.1080/01621459.2024.2337156>. Supported response families include
Gaussian, binomial, Poisson, negative binomial, gamma, beta, ordered beta,
ordinal (cumulative link), multinomial, zero-inflated counts, a Tweedie
compound Poisson for a non-negative response with a point mass at zero,
accelerated failure time and proportional hazards models for
right-censored survival data, location-scale regression, and a Dirichlet
process mixture for the error distribution. Decision rules may be hard, as
in standard BART, or soft, as in the SoftBart model of Linero and Yang
(2018) <doi:10.1111/rssb.12293>, which yields smoother fits. The interface
follows that of glm(), so that a model is specified with a formula, a data
frame, and a family.

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
