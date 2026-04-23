%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  llmclean
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'LLM'-Assisted Data Cleaning with Multi-Provider Support

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-stats 
Requires:         R-utils 

%description
Detects and suggests fixes for semantic inconsistencies in data frames by
calling large language models (LLMs) through a unified, provider-agnostic
interface. Supported providers include 'OpenAI' ('GPT-4o', 'GPT-4o-mini'),
'Anthropic' ('Claude'), 'Google' ('Gemini'), 'Groq' (free-tier 'LLaMA' and
'Mixtral'), and local 'Ollama' models. The package identifies issues that
rule-based tools cannot detect: abbreviation variants, typographic errors,
case inconsistencies, and malformed values. Results are returned as tidy
data frames with column, row index, detected value, issue type, suggested
fix, and confidence score. An offline fallback using statistical and
fuzzy-matching methods is provided for use without any API key.
Interactive fix application with human review is supported via
'apply_fixes()'. Methods follow de Jonge and van der Loo (2013)
<https://cran.r-project.org/doc/contrib/de_Jonge+van_der_Loo-Introduction_to_data_cleaning_with_R.pdf>
and Chaudhuri et al. (2003) <doi:10.1145/872757.872796>.

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
