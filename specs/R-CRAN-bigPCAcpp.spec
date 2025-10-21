%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigPCAcpp
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Principal Component Analysis for 'bigmemory' Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-methods 
Requires:         R-CRAN-withr 

%description
High performance principal component analysis routines that operate
directly on 'bigmemory::big.matrix' objects. The package avoids
materialising large matrices in memory by streaming data through 'BLAS'
and 'LAPACK' kernels and provides helpers to derive scores, loadings,
correlations, and contribution diagnostics, including utilities that
stream results into 'bigmemory'-backed matrices for file-based workflows.
Additional interfaces expose 'scalable' singular value decomposition,
robust PCA, and robust SVD algorithms so that users can explore large
matrices while tempering the influence of outliers. 'Scalable' principal
component analysis is also implemented, Elgamal, Yabandeh, Aboulnaga,
Mustafa, and Hefeeda (2015) <doi:10.1145/2723372.2751520>.

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
