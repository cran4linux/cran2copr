%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tinyshinyserver
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tiny 'shiny' Server - Lightweight Multi-App 'shiny' Proxy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.7.0
BuildRequires:    R-CRAN-curl >= 3.3
BuildRequires:    R-CRAN-ps >= 1.7.0
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-httpuv >= 1.5.5
BuildRequires:    R-CRAN-later >= 1.4.0
BuildRequires:    R-CRAN-websocket >= 1.1.0
BuildRequires:    R-CRAN-logger >= 0.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-callr >= 3.7.0
Requires:         R-CRAN-curl >= 3.3
Requires:         R-CRAN-ps >= 1.7.0
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-httpuv >= 1.5.5
Requires:         R-CRAN-later >= 1.4.0
Requires:         R-CRAN-websocket >= 1.1.0
Requires:         R-CRAN-logger >= 0.2.0
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-quarto 
Requires:         R-tools 
Requires:         R-utils 

%description
A lightweight proxy server that hosts multiple 'shiny' applications,
including interactive 'R Markdown' documents and 'Quarto' dashboards, each
in its own R process. It forwards HTTP and 'WebSocket' traffic, keeps apps
running or starts them on demand, restarts failed apps, and provides a web
dashboard for monitoring and management. The server is configured with a
JSON file.

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
