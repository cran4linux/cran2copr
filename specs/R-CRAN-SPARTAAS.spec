%global __brp_check_rpaths %{nil}
%global packname  SPARTAAS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Archaeology

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-explor 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-scatterD3 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-mapview 
Requires:         R-CRAN-FactoMineR 
Requires:         R-grDevices 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyjqui 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-explor 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-scatterD3 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-maptools 
Requires:         R-grid 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-mapview 

%description
Statistical pattern recognition and dating using archaeological artefacts
assemblages. Package of statistical tools for archaeology.
hclustcompro(perioclust): Bellanger Lise, Coulon Arthur, Husi Philippe
(2020, ISBN:978-3-030-60103-4). seriograph: Bruno Desachy (2004)
<doi:10.3406/pica.2004.2396>.

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
