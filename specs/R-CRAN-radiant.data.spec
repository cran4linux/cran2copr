%global __brp_check_rpaths %{nil}
%global packname  radiant.data
%global packver   1.3.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.12
Release:          1%{?dist}%{?buildtag}
Summary:          Data Menu for Radiant: Business Analytics using R and Shiny

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-CRAN-car >= 3.0.0
BuildRequires:    R-CRAN-curl >= 2.5
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-psych >= 1.8.4
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-stringi >= 1.2.4
BuildRequires:    R-CRAN-rmarkdown >= 1.14
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-import >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.1
BuildRequires:    R-CRAN-readxl >= 1.0.0
BuildRequires:    R-CRAN-patchwork >= 1.0.0
BuildRequires:    R-CRAN-markdown >= 1.0
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-DT >= 0.9
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-shinyFiles >= 0.7.3
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-broom >= 0.5.2
BuildRequires:    R-CRAN-shinyAce >= 0.4.1
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-scales >= 0.4.0
BuildRequires:    R-CRAN-randomizr >= 0.20.0
BuildRequires:    R-CRAN-writexl >= 0.2
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-CRAN-car >= 3.0.0
Requires:         R-CRAN-curl >= 2.5
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-psych >= 1.8.4
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-stringi >= 1.2.4
Requires:         R-CRAN-rmarkdown >= 1.14
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-import >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.1
Requires:         R-CRAN-readxl >= 1.0.0
Requires:         R-CRAN-patchwork >= 1.0.0
Requires:         R-CRAN-markdown >= 1.0
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-DT >= 0.9
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-shinyFiles >= 0.7.3
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-broom >= 0.5.2
Requires:         R-CRAN-shinyAce >= 0.4.1
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-randomizr >= 0.20.0
Requires:         R-CRAN-writexl >= 0.2
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-base64enc 

%description
The Radiant Data menu includes interfaces for loading, saving, viewing,
visualizing, summarizing, transforming, and combining data. It also
contains functionality to generate reproducible reports of the analyses
conducted in the application.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
