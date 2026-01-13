%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  exdqlm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Dynamic Quantile Linear Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-crch 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-HyperbolicDist 
BuildRequires:    R-CRAN-GeneralizedHyperbolic 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-crch 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-HyperbolicDist 
Requires:         R-CRAN-GeneralizedHyperbolic 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-grDevices 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-matrixStats 

%description
Routines for Bayesian estimation and analysis of dynamic quantile linear
models utilizing the extended asymmetric Laplace error distribution, also
known as extended dynamic quantile linear models (exDQLM) described in
Barata et al (2020) <doi:10.1214/21-AOAS1497>.

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
