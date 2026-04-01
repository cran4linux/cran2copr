%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aisdk
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Interface for AI Model Providers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-digest 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-openssl 

%description
A production-grade AI toolkit for R featuring a layered architecture
(Specification, Utilities, Providers, Core), request interception support,
robust error handling with exponential retry delays, support for multiple
AI model providers ('OpenAI', 'Anthropic', etc.), local small language
model inference, distributed 'MCP' ecosystem, multi-agent orchestration,
progressive knowledge loading through skills, and a global skill store for
sharing AI capabilities.

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
