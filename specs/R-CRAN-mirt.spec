%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mirt
%global packver   1.44.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.44.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Item Response Theory

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-pbapply >= 1.3.0
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-dcurver 
BuildRequires:    R-CRAN-SimDesign 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-pbapply >= 1.3.0
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-CRAN-lattice 
Requires:         R-methods 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-Deriv 
Requires:         R-splines 
Requires:         R-CRAN-dcurver 
Requires:         R-CRAN-SimDesign 

%description
Analysis of discrete response data using unidimensional and
multidimensional item analysis models under the Item Response Theory
paradigm (Chalmers (2012) <doi:10.18637/jss.v048.i06>). Exploratory and
confirmatory item factor analysis models are estimated with quadrature
(EM) or stochastic (MHRM) methods. Confirmatory bi-factor and two-tier
models are available for modeling item testlets using dimension reduction
EM algorithms, while multiple group analyses and mixed effects designs are
included for detecting differential item, bundle, and test functioning,
and for modeling item and person covariates. Finally, latent class models
such as the DINA, DINO, multidimensional latent class, mixture IRT models,
and zero-inflated response models are supported, as well as a wide family
of probabilistic unfolding models.

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
