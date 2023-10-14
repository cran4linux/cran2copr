%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RTMB
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          'R' Bindings for 'TMB'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-TMB >= 1.9.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.9.5
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-MASS 

%description
Native 'R' interface to 'TMB' (Template Model Builder) so models can be
written entirely in 'R' rather than 'C++'. Automatic differentiation, to
any order, is available for a rich subset of 'R' features, including
linear algebra for dense and sparse matrices, complex arithmetic, Fast
Fourier Transform, probability distributions and special functions. 'RTMB'
provides easy access to model fitting and validation following the
principles of Kristensen, K., Nielsen, A., Berg, C. W., Skaug, H., & Bell,
B. M. (2016) <DOI:10.18637/jss.v070.i05> and Thygesen, U.H., Albertsen,
C.M., Berg, C.W. et al. (2017) <DOI:10.1007/s10651-017-0372-4>.

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
