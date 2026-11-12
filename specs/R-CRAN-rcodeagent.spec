%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcodeagent
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Coding Assistant for 'RStudio' with 'ChatGPT' Authentication

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jose >= 2.0.0
BuildRequires:    R-CRAN-httr2 >= 1.2.0
BuildRequires:    R-CRAN-filelock >= 1.0.3
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-sodium 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-later 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
Requires:         R-CRAN-jose >= 2.0.0
Requires:         R-CRAN-httr2 >= 1.2.0
Requires:         R-CRAN-filelock >= 1.0.3
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-sodium 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-later 
Requires:         R-utils 
Requires:         R-grid 

%description
Provides an interactive coding assistant in the 'RStudio' Viewer to
explain R code, draft scripts, and propose changes to a selected editor
target. Supports read-only chat, explicitly authorized edits, and
user-requested submission of code to the native R console. Authenticates
through 'ChatGPT' using browser-based OAuth 2.0 authorization with Proof
Key for Code Exchange (PKCE) and stores credentials using the operating
system credential store. Model requests require Internet access and an
eligible 'ChatGPT' Plus or Pro account under the service's current terms
<https://developers.openai.com/siwc/quickstart>. Neither an API key nor
'Codex CLI' is required.

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
