%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ellmercodex
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          'ChatGPT' Plan Provider for 'ellmer'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.3.0
BuildRequires:    R-CRAN-ellmer >= 0.5.0
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-jose 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-S7 
Requires:         R-CRAN-httr2 >= 1.3.0
Requires:         R-CRAN-ellmer >= 0.5.0
Requires:         R-CRAN-coro 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-jose 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-S7 

%description
Connects 'ellmer' chats to a 'ChatGPT' subscription through 'OpenAI''s
documented "Sign in with ChatGPT" flow for open-source, locally hosted
apps <https://developers.openai.com/siwc/token-sharing-open-source>.
Provides a stable, explicitly bounded core of the public 'ellmer' (>=
0.5.0) Chat object, including browser sign-in with dynamic client
registration, package-scoped credential storage, redacted diagnostics,
multi-turn text, streaming, structured-output, function-tool,
asynchronous, cancellation, cloning, metadata, multimodal chat,
account-specific model discovery, and reasoning-effort selection through
the public 'Responses' API. Parallel and batch helper functions are
explicitly unsupported because 'ChatGPT' plan usage is stream-only. This
independent third-party integration is not endorsed by 'OpenAI'.

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
