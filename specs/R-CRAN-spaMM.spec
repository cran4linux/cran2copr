%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spaMM
%global packver   4.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed-Effect Models, with or without Spatial Random Effects

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-gmp >= 0.6.0
BuildRequires:    R-CRAN-geometry >= 0.4.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-gmp >= 0.6.0
Requires:         R-CRAN-geometry >= 0.4.0
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-numDeriv 

%description
Inference based on models with or without spatially-correlated random
effects, multivariate responses, or non-Gaussian random effects (e.g.,
Beta). Variation in residual variance (heteroscedasticity) can itself be
represented by a mixed-effect model. Both classical geostatistical models
(Rousset and Ferdy 2014 <doi:10.1111/ecog.00566>), and Markov random field
models on irregular grids (as considered in the 'INLA' package,
<https://www.r-inla.org>), can be fitted, with distinct computational
procedures exploiting the sparse matrix representations for the latter
case and other autoregressive models. Laplace approximations are used for
likelihood or restricted likelihood. Penalized quasi-likelihood and other
variants discussed in the h-likelihood literature (Lee and Nelder 2001
<doi:10.1093/biomet/88.4.987>) are also implemented.

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
