%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jack
%global packver   5.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Jack, Zonal, and Schur Polynomials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-JuliaConnectoR 
BuildRequires:    R-CRAN-multicool 
BuildRequires:    R-CRAN-mvp 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-qspray 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Ryacas 
BuildRequires:    R-CRAN-spray 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-JuliaConnectoR 
Requires:         R-CRAN-multicool 
Requires:         R-CRAN-mvp 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-qspray 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Ryacas 
Requires:         R-CRAN-spray 

%description
Symbolic calculation and evaluation of the Jack polynomials, zonal
polynomials, and Schur polynomials. Mainly based on Demmel & Koev's paper
(2006) <doi:10.1090/S0025-5718-05-01780-1>. Zonal polynomials and Schur
polynomials are particular cases of Jack polynomials. Zonal polynomials
appear in random matrix theory. Schur polynomials appear in the field of
combinatorics.

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
