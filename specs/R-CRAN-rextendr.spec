%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rextendr
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Build 'Rust' Powered 'R' Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       cargo
BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-glue >= 1.7.0
BuildRequires:    R-CRAN-pkgbuild >= 1.4.0
BuildRequires:    R-CRAN-rlang >= 1.0.5
BuildRequires:    R-CRAN-brio 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-glue >= 1.7.0
Requires:         R-CRAN-pkgbuild >= 1.4.0
Requires:         R-CRAN-rlang >= 1.0.5
Requires:         R-CRAN-brio 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-withr 

%description
Provides a framework for creating high-performance 'R' packages powered by
the 'Rust' programming language using the 'extendr' Rust crate.  It offers
'usethis'-like functions to scaffold and develop 'Rust' powered 'R'
packages, including utilities for publishing to CRAN, managing
dependencies, configuring development environments, and rendering 'Rust'
code in 'knitr' documents. Additionally, it provides functions to compile
and evaluate 'Rust' code directly from 'R' for interactive development.

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
