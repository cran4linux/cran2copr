%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  telegramR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interact with the 'Telegram' 'MTProto' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-openssl >= 2.2.2
BuildRequires:    R-CRAN-jsonlite >= 1.8.9
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.37
BuildRequires:    R-CRAN-base64enc >= 0.1.3
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-callr 
Requires:         R-CRAN-openssl >= 2.2.2
Requires:         R-CRAN-jsonlite >= 1.8.9
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.37
Requires:         R-CRAN-base64enc >= 0.1.3
Requires:         R-CRAN-R6 
Requires:         R-CRAN-future 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-later 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-callr 

%description
Provides a full-featured client for the 'Telegram' 'MTProto' protocol
(<https://core.telegram.org/api>), enabling programmatic access to
'Telegram' chats, channels, messages, media, and stories. Implements
binary encoding and decoding of the 'Telegram' 'TL' (Type Language)
schema, authentication (including two-factor), encrypted transport, and
high-level helpers for downloading channel history and reactions at scale.
Intended for social-science research and data collection tasks that
require direct API access rather than the 'Bot API'.

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
