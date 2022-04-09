%global __brp_check_rpaths %{nil}
%global packname  pkgdepends
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Package Dependency Resolution and Downloads

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-processx >= 3.4.2
BuildRequires:    R-CRAN-callr >= 3.3.1
BuildRequires:    R-CRAN-withr >= 2.1.1
BuildRequires:    R-CRAN-cli >= 2.1.0
BuildRequires:    R-CRAN-zip >= 2.1.0
BuildRequires:    R-CRAN-pkgcache >= 2.0.0
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-prettyunits >= 1.1.1
BuildRequires:    R-CRAN-filelock >= 1.0.2
BuildRequires:    R-CRAN-pkgbuild >= 1.0.2
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-ps 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-processx >= 3.4.2
Requires:         R-CRAN-callr >= 3.3.1
Requires:         R-CRAN-withr >= 2.1.1
Requires:         R-CRAN-cli >= 2.1.0
Requires:         R-CRAN-zip >= 2.1.0
Requires:         R-CRAN-pkgcache >= 2.0.0
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-prettyunits >= 1.1.1
Requires:         R-CRAN-filelock >= 1.0.2
Requires:         R-CRAN-pkgbuild >= 1.0.2
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-ps 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rprojroot 
Requires:         R-stats 
Requires:         R-utils 

%description
Find recursive dependencies of 'R' packages from various sources. Solve
the dependencies to obtain a consistent set of packages to install.
Download packages, and install them. It supports packages on 'CRAN',
'Bioconductor' and other 'CRAN-like' repositories, 'GitHub', package
'URLs', and local package trees and files. It caches metadata and package
files via the 'pkgcache' package, and performs all 'HTTP' requests,
downloads, builds and installations in parallel. 'pkgdepends' is the
workhorse of the 'pak' package.

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
