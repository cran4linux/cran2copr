%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  V8
%global packver   6.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Embedded JavaScript and WebAssembly Engine for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    v8-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-curl >= 1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-curl >= 1.0
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-utils 

%description
An R interface to V8 <https://v8.dev>: Google's open source JavaScript and
WebAssembly engine. This package can be compiled either with V8 version 6
and up or NodeJS when built as a shared library.

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
