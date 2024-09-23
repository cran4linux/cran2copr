%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bit64
%global packver   4.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          A S3 Class for Vectors of 64bit Integers

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-bit >= 4.0.0
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-bit >= 4.0.0
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-stats 

%description
Package 'bit64' provides serializable S3 atomic 64bit (signed) integers.
These are useful for handling database keys and exact counting in +-2^63.
WARNING: do not use them as replacement for 32bit integers, integer64 are
not supported for subscripting by R-core and they have different semantics
when combined with double, e.g. integer64 + double => integer64. Class
integer64 can be used in vectors, matrices, arrays and data.frames.
Methods are available for coercion from and to logicals, integers,
doubles, characters and factors as well as many elementwise and summary
functions. Many fast algorithmic operations such as 'match' and 'order'
support inter- active data exploration and manipulation and optionally
leverage caching.

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
