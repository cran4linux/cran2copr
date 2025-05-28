%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastmatrix
%global packver   0.5-9017
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.9017
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Computation of some Matrices Useful in Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
Small set of functions to fast computation of some matrices and operations
useful in statistics and econometrics. Currently, there are functions for
efficient computation of duplication, commutation and symmetrizer matrices
with minimal storage requirements. Some commonly used matrix
decompositions (LU and LDL), basic matrix operations (for instance,
Hadamard, Kronecker products and the Sherman-Morrison formula) and
iterative solvers for linear systems are also available. In addition, the
package includes a number of common statistical procedures such as the
sweep operator, weighted mean and covariance matrix using an online
algorithm, linear regression (using Cholesky, QR, SVD, sweep operator and
conjugate gradients methods), ridge regression (with optimal selection of
the ridge parameter considering several procedures), omnibus tests for
univariate normality, functions to compute the multivariate skewness,
kurtosis, the Mahalanobis distance (checking the positive defineteness),
and the Wilson-Hilferty transformation of gamma variables. Furthermore,
the package provides interfaces to C code callable by another C code from
other R packages.

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
