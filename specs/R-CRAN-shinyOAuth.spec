%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyOAuth
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Provider-Agnostic OAuth Authentication for 'shiny' Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-openssl >= 2.0.0
BuildRequires:    R-CRAN-R6 >= 2.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-jose >= 1.2.0
BuildRequires:    R-CRAN-cachem >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-CRAN-S7 >= 0.2.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-openssl >= 2.0.0
Requires:         R-CRAN-R6 >= 2.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-jose >= 1.2.0
Requires:         R-CRAN-cachem >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-S7 >= 0.2.0

%description
Provides a simple, configurable, provider-agnostic 'OAuth 2.0' and 'OpenID
Connect' (OIDC) authentication framework for 'shiny' applications using
'S7' classes. Defines providers, clients, and tokens, as well as various
supporting functions and a 'shiny' module. Features include cross-site
request forgery (CSRF) protection, state encryption, 'Proof Key for Code
Exchange' (PKCE) handling, validation of OIDC identity tokens (nonces,
signatures, claims), automatic user info retrieval, asynchronous flows,
and hooks for audit logging.

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
