%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rmpfr
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface R to MPFR - Multiple Precision Floating-Point Reliable

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
BuildRequires:    mpfr-devel
BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-gmp >= 0.6.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-gmp >= 0.6.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Arithmetic (via S4 classes and methods) for arbitrary precision floating
point numbers, including transcendental ("special") functions.  To this
end, the package interfaces to the 'LGPL' licensed 'MPFR' (Multiple
Precision Floating-Point Reliable) Library which itself is based on the
'GMP' (GNU Multiple Precision) Library.

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
