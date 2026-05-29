%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  llmshieldr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Safety Guardrails for Large Language Model Workflows

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-stringi 

%description
A model-agnostic safety layer for developers building with large language
model (LLM) applications. Maps starter controls to the Open Worldwide
Application Security Project Top 10 for Large Language Model Applications
2025 risk categories <https://genai.owasp.org/llm-top-10/> via a modular
rule engine. Supports regular-expression rules, lightweight natural
language processing (NLP) intent checks, optional scanners, and semantic
large language model reviewer checks on prompts, conversations, retrieved
context, tool inputs and outputs, streaming chunks, and model outputs.
Supports workflows with the 'Ollama' local web service
<https://ollama.com/> via 'ellmer', remote reviewer endpoints, and other
chat interfaces callable from 'R'. Intended as an experimental guardrail
layer that teams should evaluate against their own workflows before
relying on it in production.

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
