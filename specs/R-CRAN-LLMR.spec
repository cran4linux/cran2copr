%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LLMR
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface for Large Language Model APIs in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-mime 
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-mime 

%description
Provides a unified interface to interact with multiple Large Language
Model (LLM) APIs. The package supports text generation, embeddings,
parallelization, as well as tidyverse integration.  Users can switch
between different LLM providers seamlessly within R workflows, or call
multiple models in parallel. The package enables creation of LLM agents
for automated tasks and provides consistent error handling across all
supported APIs. APIs include 'OpenAI' (see
<https://platform.openai.com/docs> for details), 'Anthropic' (see
<https://docs.anthropic.com/en/api/getting-started> for details), 'Groq'
(see <https://console.groq.com/docs/api-reference> for details), 'Together
AI' (see <https://docs.together.ai/docs/quickstart> for details),
'DeepSeek' (see <https://api-docs.deepseek.com> for details), 'Gemini'
(see <https://aistudio.google.com> for details), 'xAI' (see
<https://docs.x.ai/> for details), and 'Voyage AI' (see
<https://docs.voyageai.com/docs/introduction> for details).

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
