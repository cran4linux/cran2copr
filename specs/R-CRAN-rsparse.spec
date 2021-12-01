%global __brp_check_rpaths %{nil}
%global packname  rsparse
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Learning on Sparse Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Matrix >= 1.3
BuildRequires:    R-CRAN-data.table >= 1.10.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.100.5.0
BuildRequires:    R-CRAN-float >= 0.2.2
BuildRequires:    R-CRAN-lgr >= 0.2
BuildRequires:    R-CRAN-Rcpp >= 0.11
BuildRequires:    R-CRAN-MatrixExtra >= 0.1.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-Matrix >= 1.3
Requires:         R-CRAN-data.table >= 1.10.0
Requires:         R-CRAN-float >= 0.2.2
Requires:         R-CRAN-lgr >= 0.2
Requires:         R-CRAN-Rcpp >= 0.11
Requires:         R-CRAN-MatrixExtra >= 0.1.7
Requires:         R-methods 
Requires:         R-CRAN-RhpcBLASctl 

%description
Implements many algorithms for statistical learning on sparse matrices -
matrix factorizations, matrix completion, elastic net regressions,
factorization machines. Also 'rsparse' enhances 'Matrix' package by
providing methods for multithreaded <sparse, dense> matrix products and
native slicing of the sparse matrices in Compressed Sparse Row (CSR)
format. List of the algorithms for regression problems: 1) Elastic Net
regression via Follow The Proximally-Regularized Leader (FTRL) Stochastic
Gradient Descent (SGD), as per McMahan et al(,
<doi:10.1145/2487575.2488200>) 2) Factorization Machines via SGD, as per
Rendle (2010, <doi:10.1109/ICDM.2010.127>) List of algorithms for matrix
factorization and matrix completion: 1) Weighted Regularized Matrix
Factorization (WRMF) via Alternating Least Squares (ALS) - paper by Hu,
Koren, Volinsky (2008, <doi:10.1109/ICDM.2008.22>) 2) Maximum-Margin
Matrix Factorization via ALS, paper by Rennie, Srebro (2005,
<doi:10.1145/1102351.1102441>) 3) Fast Truncated Singular Value
Decomposition (SVD), Soft-Thresholded SVD, Soft-Impute matrix completion
via ALS - paper by Hastie, Mazumder et al. (2014, <arXiv:1410.2596>) 4)
Linear-Flow matrix factorization, from 'Practical linear models for
large-scale one-class collaborative filtering' by Sedhain, Bui, Kawale et
al (2016, ISBN:978-1-57735-770-4) 5) GlobalVectors (GloVe) matrix
factorization via SGD, paper by Pennington, Socher, Manning (2014,
<https://aclanthology.org/D14-1162/>) Package is reasonably fast and
memory efficient - it allows to work with large datasets - millions of
rows and millions of columns. This is particularly useful for
practitioners working on recommender systems.

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
