%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CARBayes
%global packver   6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Generalised Linear Mixed Models for Areal Unit Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-CARBayesdata 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-CARBayesdata 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-mapview 
Requires:         R-CRAN-MCMCpack 
Requires:         R-parallel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-CRAN-truncnorm 
Requires:         R-utils 

%description
Implements a class of univariate and multivariate spatial generalised
linear mixed models for areal unit data, with inference in a Bayesian
setting using Markov chain Monte Carlo (MCMC) simulation using a single or
multiple Markov chains. The response variable can be binomial, Gaussian,
multinomial, Poisson or zero-inflated Poisson (ZIP), and spatial
autocorrelation is modelled by a set of random effects that are assigned a
conditional autoregressive (CAR) prior distribution. A number of different
models are available for univariate spatial data, including models with no
random effects as well as random effects modelled by different types of
CAR prior, including the BYM model (Besag et al., 1991,
<doi:10.1007/BF00116466>) and Leroux model (Leroux et al., 2000,
<doi:10.1007/978-1-4612-1284-3_4>). Additionally, a multivariate CAR
(MCAR) model for multivariate spatial data is available, as is a two-level
hierarchical model for modelling data relating to individuals within
areas. Full details are given in the vignette accompanying this package.
The initial creation of this package was supported by the Economic and
Social Research Council (ESRC) grant RES-000-22-4256, and on-going
development has been supported by the Engineering and Physical Science
Research Council (EPSRC) grant EP/J017442/1, ESRC grant ES/K006460/1,
Innovate UK / Natural Environment Research Council (NERC) grant
NE/N007352/1 and the TB Alliance.

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
