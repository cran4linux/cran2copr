%global __brp_check_rpaths %{nil}
%global packname  epitweetr
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Early Detection of Public Health Threats from Twitter Data

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-emayili 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rtweet 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rnaturalearthdata 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-future 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-emayili 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-magrittr 
Requires:         R-parallel 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rtweet 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rnaturalearthdata 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-tokenizers 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-xml2 

%description
It allows you to automatically monitor trends of tweets by time, place and
topic aiming at detecting public health threats early through the
detection of signals (e.g. an unusual increase in the number of tweets).
It was designed to focus on infectious diseases, and it can be extended to
all hazards or other fields of study by modifying the topics and keywords.

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
