%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tinylens
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Minimal Implementation of Functional Lenses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-vctrs 

%description
Provides utilities to create and use lenses to simplify data manipulation.
Lenses are composable getter/setter pairs that provide a functional
approach to manipulating deeply nested data structures, e.g., elements
within list columns in data frames. The implementation is based on the
earlier 'lenses' R package <https://github.com/cfhammill/lenses>, which
was inspired by the Haskell 'lens' package by Kmett (2012)
<https://github.com/ekmett/lens>, one of the most widely referenced
implementations of lenses. For additional background and history on the
theory of lenses, see the 'lens' package wiki:
<https://github.com/ekmett/lens/wiki/History-of-Lenses>.

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
