%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chatRater
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rating and Evaluating Texts Using Large Language Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-openai 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-openai 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 

%description
Generates ratings and psycholinguistic metrics for textual stimuli using
large language models. It enables users to evaluate idioms and other
language materials by combining context, prompts, and stimulus inputs. It
supports multiple LLM APIs (such as 'OpenAI', 'DeepSeek', 'Anthropic',
'Cohere', 'Google PaLM', and 'Ollama') by allowing users to switch models
with a single parameter. In addition to generating numeric ratings,
'chatRater' provides functions for obtaining detailed psycholinguistic
metrics including word frequency (with optional corpus input), lexical
coverage (with customizable vocabulary size and test basis), Zipf metric,
Levenshtein distance, and semantic transparency.

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
