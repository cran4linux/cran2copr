%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesammi
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of the Additive Main Effects and Multiplicative Interaction Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Bayesian estimation of the additive main effects and multiplicative
interaction (AMMI) model of multi-environment trials by the Gibbs sampler
of Crossa, Perez-Elizalde, Jarquin, Cotes, Viele, Liu and Cornelius (2011)
<doi:10.2135/cropsci2010.06.0343>: posterior distributions of the overall
mean, genotype and environment effects, singular values, genotype and
environment scores (von Mises-Fisher conditionals on the constrained
spheres) and error variance; several chains with burn-in and thinning;
posterior summaries with highest posterior density intervals; the
convergence diagnostics of Raftery-Lewis, Heidelberger-Welch and
Gelman-Rubin; the AMMI biplot with highest posterior density regions for
inference on genotypes and environments; least-squares AMMI; and a
plain-language interpretation of every result, computed from its numbers.
Beyond the article: unbalanced trials with missing plots and cells (data
augmentation), environment-specific error variances, the Bayesian GGE
(sites regression) model of Perez-Elizalde, Jarquin and Crossa (2012)
<doi:10.1007/s13253-011-0063-9>, probabilities of superior performance and
stability (Dias et al. 2022 <doi:10.1007/s00122-022-04041-y>), posterior
ranks, Bayesian stability measures, predictions and the winner of every
environment, model choice by DIC and WAIC with posterior predictive
checks, draws for the 'posterior', 'bayesplot' and 'coda' packages, a
compiled sampler, and a built-in 'shiny' application. Bayesian stability
analysis: the Finlay-Wilkinson, Eberhart-Russell and Shukla models by
Gibbs sampling, and the posterior distributions of classical stability
indices (Wricke, Shukla, Lin-Binns, Annicchiarico, Eskridge's
safety-first) and of AMMI-based indices (ASV, SIPC, EV, Za, WAAS, WAASY).
Every result prints the references of its method.

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
