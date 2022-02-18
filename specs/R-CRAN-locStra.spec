%global __brp_check_rpaths %{nil}
%global packname  locStra
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Implementation of (Local) Population Stratification Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-RSpectra 

%description
Fast implementations to compute the genetic covariance matrix, the Jaccard
similarity matrix, the s-matrix (the weighted Jaccard similarity matrix),
and the (classic or robust) genomic relationship matrix of a (dense or
sparse) input matrix (see Hahn, Lutz, Hecker, Prokopenko, Cho, Silverman,
Weiss, and Lange (2020) <doi:10.1002/gepi.22356>). Full support for sparse
matrices from the R-package 'Matrix'. Additionally, an implementation of
the power method (von Mises iteration) to compute the largest eigenvector
of a matrix is included, a function to perform an automated full run of
global and local correlations in population stratification data, a
function to compute sliding windows, and a function to invert minor
alleles and to select those variants/loci exceeding a minimal cutoff
value. New functionality in locStra allows one to extract the k leading
eigenvectors of the genetic covariance matrix, Jaccard similarity matrix,
s-matrix, and genomic relationship matrix without actually computing the
similarity matrices.

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
