%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jack
%global packver   6.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Jack, Zonal, Schur, and Other Symmetric Polynomials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-qspray >= 3.1.0
BuildRequires:    R-CRAN-ratioOfQsprays >= 1.1.0
BuildRequires:    R-CRAN-symbolicQspray >= 1.1.0
BuildRequires:    R-CRAN-syt >= 0.5.0
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-multicool 
BuildRequires:    R-CRAN-mvp 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-RationalMatrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-spray 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppCGAL 
Requires:         R-CRAN-qspray >= 3.1.0
Requires:         R-CRAN-ratioOfQsprays >= 1.1.0
Requires:         R-CRAN-symbolicQspray >= 1.1.0
Requires:         R-CRAN-syt >= 0.5.0
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-gmp 
Requires:         R-methods 
Requires:         R-CRAN-multicool 
Requires:         R-CRAN-mvp 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-RationalMatrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-spray 
Requires:         R-utils 

%description
Schur polynomials appear in combinatorics and zonal polynomials appear in
random matrix theory. They are particular cases of Jack polynomials. This
package allows to compute these polynomials and other symmetric
multivariate polynomials: flagged Schur polynomials, factorial Schur
polynomials, t-Schur polynomials, Hall-Littlewood polynomials, Macdonald
polynomials, and modified Macdonald polynomials. In addition, it can
compute the Kostka-Jack numbers, the Kostka-Foulkes polynomials, the
Kostka-Macdonald polynomials, and the Hall polynomials.  Mainly based on
Demmel & Koev's paper (2006) <doi:10.1090/S0025-5718-05-01780-1> and
Macdonald's book (1995) <doi:10.1093/oso/9780198534891.003.0001>.

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
