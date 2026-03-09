%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pMEM
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive Moran's Eigenvector Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-sf 

%description
Calculate Predictive Moran's Eigenvector Maps (pMEM) for
spatially-explicit prediction of environmental variables, as defined by
Guénard and Legendre (2024) <doi:10.1111/2041-210X.14413>. pMEM extends
classical MEM by enabling interpolation and prediction at unsampled
locations using spatial weighting functions parameterized by range (and
optionally shape). The package implements multiple pMEM types (e.g.,
exponential, Gaussian, linear) and features a modular architecture that
allows programmers to define custom weighting functions. Designed for
ecologists, geographers, and spatial analysts working with
spatially-structured data.

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
