%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  momentuHMM
%global packver   1.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Analysis of Animal Movement Behavior Using Multivariate Hidden Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-crawl >= 2.2.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Brobdingnag 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-crawl >= 2.2.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Brobdingnag 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-raster 

%description
Extended tools for analyzing telemetry data using generalized hidden
Markov models. Features of momentuHMM (pronounced ``momentum'') include
data pre-processing and visualization, fitting HMMs to location and
auxiliary biotelemetry or environmental data, biased and correlated random
walk movement models, hierarchical HMMs, multiple imputation for
incorporating location measurement error and missing data, user-specified
design matrices and constraints for covariate modelling of parameters,
random effects, decoding of the state process, visualization of fitted
models, model checking and selection, and simulation. See McClintock and
Michelot (2018) <doi:10.1111/2041-210X.12995>.

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
