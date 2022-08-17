%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fiery
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Lightweight and Flexible Web Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-reqres 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-uuid 
Requires:         R-utils 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-future 
Requires:         R-CRAN-later 
Requires:         R-stats 
Requires:         R-CRAN-reqres 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-crayon 

%description
A very flexible framework for building server side logic in R. The
framework is unopinionated when it comes to how HTTP requests and
WebSocket messages are handled and supports all levels of app complexity;
from serving static content to full-blown dynamic web-apps. Fiery does not
hold your hand as much as e.g. the shiny package does, but instead sets
you free to create your web app the way you want.

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
