%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tinyshinyserver
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tiny 'shiny' Server - Lightweight Multi-App 'shiny' Proxy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-websocket 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-quarto 
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-later 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-websocket 
Requires:         R-CRAN-future 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-quarto 

%description
A lightweight, 'WebSocket'-enabled proxy server for hosting multiple
'shiny' applications with automatic health monitoring, session management,
and resource cleanup. Provides a simple entry point to run the server
using a JSON configuration file.

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
