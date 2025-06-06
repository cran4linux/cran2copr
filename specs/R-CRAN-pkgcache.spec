%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkgcache
%global packver   2.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Cache 'CRAN'-Like Metadata and R Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-processx >= 3.3.0.9001
BuildRequires:    R-CRAN-cli >= 3.2.0
BuildRequires:    R-CRAN-curl >= 3.2
BuildRequires:    R-CRAN-callr >= 2.0.4.9000
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-processx >= 3.3.0.9001
Requires:         R-CRAN-cli >= 3.2.0
Requires:         R-CRAN-curl >= 3.2
Requires:         R-CRAN-callr >= 2.0.4.9000
Requires:         R-CRAN-filelock 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-R6 
Requires:         R-tools 
Requires:         R-utils 

%description
Metadata and package cache for CRAN-like repositories.  This is a utility
package to be used by package management tools that want to take advantage
of caching.

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
