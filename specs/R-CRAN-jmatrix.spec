%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jmatrix
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read from/Write to Disk Matrices with any Data Type in a Binary Format

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-memuse >= 4.2.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-memuse >= 4.2.1
Requires:         R-CRAN-Rcpp >= 1.0.8

%description
A mainly instrumental package meant to allow other packages whose core is
written in 'C++' to read, write and manipulate matrices in a binary format
so that the memory used for them is no more than strictly needed. Its
functionality is already inside 'parallelpam' and 'scellpam', so if you
have installed any of these, you do not need to install 'jmatrix'. Using
just the needed memory is not always true with 'R' matrices or vectors,
since by default they are of double type. Trials like the 'float' package
have been done, but to use them you have to coerce a matrix already loaded
in 'R' memory to a float matrix, and then you can delete it. The problem
comes when your computer has not memory enough to hold the matrix in the
first place, so you are forced to load it by chunks. This is the problem
this package tries to address (with partial success, but this is a
difficult problem since 'R' is not a strictly typed language, which is
anyway quite hard to get in an interpreted language). This package allows
the creation and manipulation of full, sparse and symmetric matrices of
any standard data type.

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
