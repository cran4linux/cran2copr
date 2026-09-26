%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vasicekreg
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vasicek-Type Distributions and Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-statmod 

%description
Provides density, cumulative distribution, quantile, and random generation
functions for Vasicek-type distributions with standard normal, standard
logistic, and standard hyperbolic-secant kernels. The normal-kernel
distribution is parameterized by either its mean or a fixed quantile,
whereas the logistic- and hyperbolic-secant-kernel distributions use
fixed-quantile parameterizations. Zero-augmented, one-augmented, and
zero-and-one-augmented extensions of the normal-kernel mean
parameterization are also provided for responses that include boundary
values. The corresponding 'NVASIM', 'NVASIQ', 'LVASIQ', 'HVASIQ',
'ZANVASIM', 'OANVASIM', and 'ZOANVASIM' families are available for fitting
Generalized Additive Models for Location, Scale and Shape (GAMLSS), as
introduced by Rigby and Stasinopoulos (2005,
<doi:10.1111/j.1467-9876.2005.00510.x>). Two-part random-intercept
regression models for zero-augmented longitudinal responses are included
with either a beta or a normal-kernel Vasicek positive component,
extending the framework of Chen and Li (2016,
<doi:10.1093/bioinformatics/btw308>). Some functions are written in 'C++'
using 'Rcpp', developed by Eddelbuettel and Francois (2011,
<doi:10.18637/jss.v040.i08>).

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
