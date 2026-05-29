%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  corteza
%global packver   0.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.9
Release:          1%{?dist}%{?buildtag}
Summary:          AI Agent Runtime

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-llm.api >= 0.1.4
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-printify 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-saber 
Requires:         R-CRAN-llm.api >= 0.1.4
Requires:         R-CRAN-callr 
Requires:         R-CRAN-codetools 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-printify 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-saber 

%description
An agent runtime that gives Large Language Models (LLMs) from 'Anthropic'
<https://www.anthropic.com/>, 'OpenAI' <https://openai.com/>, 'Moonshot'
<https://www.moonshot.ai/>, and 'Ollama' <https://ollama.com/> direct
access to a live R session with managed workspace state. Tools execute as
R function calls with provenance tracking, and a deterministic retrieval
system keeps relevant objects in context across turns. Three entry points:
a shell command-line interface (CLI), a console read-eval-print-loop via
chat(), and a Model Context Protocol (MCP) server via serve() for external
clients.

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
