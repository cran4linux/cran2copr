%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyllm
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Integration of Large Language Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-S7 >= 0.2.0
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-S7 >= 0.2.0
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-grDevices 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-png 
Requires:         R-CRAN-lifecycle 

%description
A tidy interface for integrating large language model (LLM) APIs such as
'Claude', 'Openai', 'Groq','Mistral' and local models via 'Ollama' into R
workflows. The package supports text and media-based interactions,
interactive message history, batch request APIs, and a tidy,
pipeline-oriented interface for streamlined integration into data
workflows. Web services are available at <https://www.anthropic.com>,
<https://openai.com>, <https://groq.com>, <https://mistral.ai/> and
<https://ollama.com>.

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
