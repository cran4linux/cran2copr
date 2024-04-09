%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spAbundance
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Univariate and Multivariate Spatial Modeling of Species Abundance

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-methods 

%description
Fits single-species (univariate) and multi-species (multivariate)
non-spatial and spatial abundance models in a Bayesian framework using
Markov Chain Monte Carlo (MCMC). Spatial models are fit using Nearest
Neighbor Gaussian Processes (NNGPs). Details on NNGP models are given in
Datta, Banerjee, Finley, and Gelfand (2016)
<doi:10.1080/01621459.2015.1044091> and Finley, Datta, and Banerjee (2020)
<doi:10.18637/jss.v103.i05>. Fits single-species and multi-species spatial
and non-spatial versions of generalized linear mixed models (Gaussian,
Poisson, Negative Binomial), N-mixture models (Royle 2004
<doi:10.1111/j.0006-341X.2004.00142.x>) and hierarchical distance sampling
models (Royle, Dawson, Bates (2004) <doi:10.1890/03-3127>). Multi-species
spatial models are fit using a spatial factor modeling approach with NNGPs
for computational efficiency.

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
