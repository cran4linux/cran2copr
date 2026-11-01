%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gptr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Language Model Agents in Live 'R' Sessions

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 6.0.0
BuildRequires:    R-CRAN-processx >= 3.8.6
BuildRequires:    R-CRAN-cli >= 3.6.2
BuildRequires:    R-CRAN-yaml >= 2.3.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.8
BuildRequires:    R-CRAN-ps >= 1.8.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 6.0.0
Requires:         R-CRAN-processx >= 3.8.6
Requires:         R-CRAN-cli >= 3.6.2
Requires:         R-CRAN-yaml >= 2.3.0
Requires:         R-CRAN-jsonlite >= 1.8.8
Requires:         R-CRAN-ps >= 1.8.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Runs language model agents in an existing 'R' session, where generated
code can inspect and modify objects already in memory. The peter()
function supports interactive chat and programmatic calls. Conversational
models use tools and return session objects; typed decision models return
logical, character or numeric vectors with associated model probabilities.
Supports the 'Anthropic'
<https://platform.claude.com/docs/en/api/overview>, 'OpenAI'
<https://developers.openai.com/api/reference/overview> and 'Google Gemini'
<https://ai.google.dev/gemini-api/docs> APIs, 'OpenAI'-compatible
endpoints, local 'Ollama' <https://ollama.com> models, and the 'Claude
Code' and 'Codex' command line tools. Decision models include 'Jev',
hosted by 'TypeSafe AI' <https://docs.typesafe.ai/introduction>, and the
local 'Clef'. Top-level agent calls and their executed code can be
recorded in 'R' scripts, 'R Markdown' and 'Quarto' documents, or 'Jupyter'
notebooks. Recorded 'R' scripts can be replayed without model calls when
the required inputs and packages are available.

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
