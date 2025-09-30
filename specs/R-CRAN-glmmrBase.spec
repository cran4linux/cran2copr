%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmmrBase
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalised Linear Mixed Models in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstan >= 2.32.1
BuildRequires:    R-CRAN-StanHeaders >= 2.32.0
BuildRequires:    R-CRAN-rstantools >= 2.3.1.1
BuildRequires:    R-CRAN-Matrix >= 1.3.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-SparseChol >= 0.3.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstan >= 2.32.1
Requires:         R-CRAN-rstantools >= 2.3.1.1
Requires:         R-CRAN-Matrix >= 1.3.1
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rstantools

%description
Specification, analysis, simulation, and fitting of generalised linear
mixed models. Includes Markov Chain Monte Carlo Maximum likelihood and
Laplace approximation model fitting for a range of models, non-linear
fixed effect specifications, a wide range of flexible covariance functions
that can be combined arbitrarily, robust and bias-corrected standard error
estimation, power calculation, data simulation, and more. See
<https://samuel-watson.github.io/glmmr-web/> for a detailed manual.

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
