%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rvisual
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visual Data Analysis 'RStudio' 'Addin' with AI Copilot

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-readxl >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-bslib >= 0.5.0
BuildRequires:    R-CRAN-DT >= 0.28
BuildRequires:    R-CRAN-httr2 >= 0.2.3
BuildRequires:    R-CRAN-rstudioapi >= 0.13
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-readxl >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-bslib >= 0.5.0
Requires:         R-CRAN-DT >= 0.28
Requires:         R-CRAN-httr2 >= 0.2.3
Requires:         R-CRAN-rstudioapi >= 0.13
Requires:         R-CRAN-htmltools 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-utils 

%description
An 'RStudio' 'addin' providing a visual, point-and-click interface for
data manipulation and analysis, designed for users transitioning from
'SPSS' to R. Every visual action generates clean, reproducible R code
using 'tidyverse' conventions ('dplyr', 'tidyr'). Includes a context-aware
AI copilot supporting multiple 'LLM' providers ('OpenAI', 'Anthropic'
Claude, 'Google Gemini') with built-in proxy support and privacy controls.

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
