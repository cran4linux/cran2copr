%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reqres
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Powerful Classes for HTTP Requests and Responses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-brotli 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-webutils 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-sodium 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-mirai 
BuildRequires:    R-CRAN-otel 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-urltools 
Requires:         R-tools 
Requires:         R-CRAN-brotli 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-webutils 
Requires:         R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-sodium 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-mirai 
Requires:         R-CRAN-otel 

%description
In order to facilitate parsing of http requests and creating appropriate
responses this package provides two classes to handle a lot of the
housekeeping involved in working with http exchanges. The infrastructure
builds upon the 'rook' specification and is thus well suited to be
combined with 'httpuv' based web servers.

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
