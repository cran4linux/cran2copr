%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ngme2
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Latent Non-Gaussian Models with Flexible Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-fmesher 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-fmesher 
Requires:         R-stats 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-withr 

%description
Fits and analyzes linear latent non-Gaussian models for temporal, spatial,
and space-time data. The package provides model components for
autoregressive and Ornstein-Uhlenbeck processes, random walks, Matern
fields based on stochastic partial differential equations, separable and
non-separable space-time models, graph-based Matern models, bivariate
type-G fields, and user-defined sparse operators. Latent fields and
observation models can use Gaussian and non-Gaussian noise distributions,
including normal inverse Gaussian, generalized asymmetric Laplace, and
skew-t distributions. Functions are included for simulation,
likelihood-based estimation, prediction, cross-validation, convergence
diagnostics, stochastic gradient optimization, batch-means confidence
intervals, and posterior-like sampling. The modeling framework is
described in Bolin, Jin, Simas and Wallin (2026) "A Unified and
Computationally Efficient Non-Gaussian Statistical Modeling Framework"
<doi:10.48550/arXiv.2602.23987>.

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
