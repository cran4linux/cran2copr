%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  llmcoder
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          LLM-Powered Code Generation and Error Fixing for 'RStudio'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-rstudioapi >= 0.13
BuildRequires:    R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-rstudioapi >= 0.13
Requires:         R-CRAN-miniUI >= 0.1.1

%description
An 'RStudio' addin that integrates large language model (LLM) assistance
directly into the code-editing workflow. Users can generate R code from
inline comments, obtain LLM-assisted fixes for console errors, and insert
plain-English explanations of selected code blocks - all without leaving
the editor. Supports 'OpenAI', 'Anthropic' (Claude), 'DeepSeek', 'Groq',
'Together AI', 'OpenRouter', 'Ollama' (fully local, no API key required),
and any 'OpenAI'-compatible custom endpoint (e.g. 'LM Studio', 'vLLM',
'llama.cpp').

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
