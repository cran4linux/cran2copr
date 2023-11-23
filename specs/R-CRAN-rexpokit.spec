%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rexpokit
%global packver   0.26.6.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.26.6.14
Release:          1%{?dist}%{?buildtag}
Summary:          R Wrappers for EXPOKIT; Other Matrix Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 

%description
Wraps some of the matrix exponentiation utilities from EXPOKIT
(<http://www.maths.uq.edu.au/expokit/>), a FORTRAN library that is widely
recommended for matrix exponentiation (Sidje RB, 1998. "Expokit: A
Software Package for Computing Matrix Exponentials." ACM Trans. Math.
Softw. 24(1): 130-156).  EXPOKIT includes functions for exponentiating
both small, dense matrices, and large, sparse matrices (in sparse
matrices, most of the cells have value 0). Rapid matrix exponentiation is
useful in phylogenetics when we have a large number of states (as we do
when we are inferring the history of transitions between the possible
geographic ranges of a species), but is probably useful in other ways as
well. NOTE: In case FORTRAN checks temporarily get rexpokit archived on
CRAN, see archived binaries at GitHub in: nmatzke/Matzke_R_binaries
(binaries install without compilation of source code).

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
