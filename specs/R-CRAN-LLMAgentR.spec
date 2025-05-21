%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LLMAgentR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Language Model Agents in R for AI Workflows and Research

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-timetk 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-modeltime.ensemble 
BuildRequires:    R-CRAN-modeltime 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-plotly 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-timetk 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-modeltime.ensemble 
Requires:         R-CRAN-modeltime 
Requires:         R-CRAN-xml2 

%description
Provides modular, graph-based agents powered by large language models
(LLMs) for intelligent task execution in R. Supports structured workflows
for tasks such as forecasting, data visualization, feature engineering,
data wrangling, data cleaning, 'SQL', code generation, weather reporting,
and research-driven question answering. Each agent performs iterative
reasoning: recommending steps, generating R code, executing, debugging,
and explaining results. Includes built-in support for packages such as
'tidymodels', 'modeltime', 'plotly', 'ggplot2', and 'prophet'. Designed
for analysts, developers, and teams building intelligent, reproducible AI
workflows in R. Compatible with LLM providers such as 'OpenAI',
'Anthropic', 'Groq', and 'Ollama'. Inspired by the Python package
'langagent'.

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
