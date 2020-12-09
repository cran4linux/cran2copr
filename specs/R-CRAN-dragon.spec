%global packname  dragon
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Deep Time Redox Analysis of the Geobiology Ontology Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-visNetwork >= 2.0.9
BuildRequires:    R-CRAN-colorspace >= 1.4
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-cowplot >= 1.0.0
BuildRequires:    R-CRAN-colourpicker >= 1.0
BuildRequires:    R-CRAN-broom >= 0.5.6
BuildRequires:    R-CRAN-igraph >= 0.4
BuildRequires:    R-CRAN-golem >= 0.2.1
BuildRequires:    R-CRAN-DT >= 0.14
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-visNetwork >= 2.0.9
Requires:         R-CRAN-colorspace >= 1.4
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-cowplot >= 1.0.0
Requires:         R-CRAN-colourpicker >= 1.0
Requires:         R-CRAN-broom >= 0.5.6
Requires:         R-CRAN-igraph >= 0.4
Requires:         R-CRAN-golem >= 0.2.1
Requires:         R-CRAN-DT >= 0.14
Requires:         R-CRAN-config 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-htmltools 
Requires:         R-stats 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-future 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-tidyselect 

%description
Create, visualize, manipulate, and analyze bipartite mineral-chemistry
networks for set of focal element(s) across deep-time on Earth. The method
is described in Spielman and Moore (2020) <doi:10.3389/feart.2020.585087>.

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
