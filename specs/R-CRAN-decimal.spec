%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  decimal
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exact Arbitrary-Precision Decimal Vectors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-withr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-withr 

%description
Arbitrary-precision vectors with an exact decimal representation, avoiding
the rounding surprises of binary floating point. Built on the 'mpdecimal'
C library, arithmetic is governed by an explicit decimal context
controlling precision, rounding, and signalling, and vectors integrate
with 'vctrs' for use in data frames, 'tibble' objects, summaries, and
common numeric workflows. Missing values, signed zeros, infinities, and
not-a-number values are supported throughout. The arithmetic model follows
Cowlishaw (2009) "General Decimal Arithmetic"
<https://speleotrove.com/decimal/decarith.html>.

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
