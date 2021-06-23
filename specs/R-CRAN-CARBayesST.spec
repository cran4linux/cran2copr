%global __brp_check_rpaths %{nil}
%global packname  CARBayesST
%global packver   3.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Generalised Linear Mixed Models for Areal Unit Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-CARBayesdata 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-CARBayesdata 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-truncnorm 
Requires:         R-utils 

%description
Implements a class of univariate and multivariate spatio-temporal
generalised linear mixed models for areal unit data, with inference in a
Bayesian setting using Markov chain Monte Carlo (MCMC) simulation. The
response variable can be binomial, Gaussian, or Poisson, but for some
models only the binomial and Poisson data likelihoods are available. The
spatio-temporal autocorrelation is modelled by random effects, which are
assigned conditional autoregressive (CAR) style prior distributions. A
number of different random effects structures are available, including
models similar to Bernardinelli et al. (1995) <doi:10.1002/sim.4780142112>
and Rushworth et al. (2014) <doi:10.1016/j.sste.2014.05.001>. Full details
are given in the vignette accompanying this package. The creation and
development of this package was supported by the Engineering and Physical
Sciences Research Council (EPSRC) grants EP/J017442/1 and EP/T004878/1 and
the Medical Research Council (MRC) grant MR/L022184/1.

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
