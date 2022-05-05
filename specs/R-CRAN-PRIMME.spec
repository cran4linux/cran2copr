%global __brp_check_rpaths %{nil}
%global packname  PRIMME
%global packver   3.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Eigenvalues and Singular Values and Vectors from Large Matrices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 

%description
R interface to 'PRIMME' <https://www.cs.wm.edu/~andreas/software/>, a C
library for computing a few eigenvalues and their corresponding
eigenvectors of a real symmetric or complex Hermitian matrix, or
generalized Hermitian eigenproblem.  It can also compute singular values
and vectors of a square or rectangular matrix. 'PRIMME' finds largest,
smallest, or interior singular/eigenvalues and can use preconditioning to
accelerate convergence. General description of the methods are provided in
the papers Stathopoulos (2010, <doi:10.1145/1731022.1731031>) and Wu
(2017, <doi:10.1137/16M1082214>). See 'citation("PRIMME")' for details.

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
