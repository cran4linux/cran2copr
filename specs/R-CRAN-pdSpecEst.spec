%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pdSpecEst
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          An Analysis Toolbox for Hermitian Positive Definite Matrices

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.500.0.0
BuildRequires:    R-CRAN-multitaper 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ddalpha 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-multitaper 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ddalpha 
Requires:         R-CRAN-Rdpack 

%description
An implementation of data analysis tools for samples of symmetric or
Hermitian positive definite matrices, such as collections of covariance
matrices or spectral density matrices. The tools in this package can be
used to perform: (i) intrinsic wavelet transforms for curves (1D) or
surfaces (2D) of Hermitian positive definite matrices with applications to
dimension reduction, denoising and clustering in the space of Hermitian
positive definite matrices; and (ii) exploratory data analysis and
inference for samples of positive definite matrices by means of intrinsic
data depth functions and rank-based hypothesis tests in the space of
Hermitian positive definite matrices.

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
