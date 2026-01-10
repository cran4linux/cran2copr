%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nnmf
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonnegative Matrix Factorization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-sparcl 
BuildRequires:    R-stats 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-osqp 
Requires:         R-parallel 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-sparcl 
Requires:         R-stats 

%description
Nonnegative matrix factorization (NMF) is a technique to factorize a
matrix with nonnegative values into the product of two matrices. Parallel
computing is an option to enhance the speed and high-dimensional and large
scale (and/or sparse) data are allowed. Relevant papers include: Wang Y.
X. and Zhang Y. J. (2012). Nonnegative matrix factorization: A
comprehensive review. IEEE Transactions on Knowledge and Data Engineering,
25(6), 1336-1353 <doi:10.1109/TKDE.2012.51> and Kim H. and Park H. (2008).
Nonnegative matrix factorization based on alternating nonnegativity
constrained least squares and active set method. SIAM Journal on Matrix
Analysis and Applications, 30(2), 713-730 <doi:10.1137/07069239X>.

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
