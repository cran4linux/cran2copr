%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stCEG
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fully Customizable Chain Event Graphs over Spatial Areas

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-hwep 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-sortable 
BuildRequires:    R-CRAN-spData 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-hwep 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyjqui 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-sortable 
Requires:         R-CRAN-spData 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-zoo 

%description
Enables the creation of Chain Event Graphs over spatial areas, with an
optional 'Shiny' user interface. Allows users to fully customise both the
structure and underlying model of the Chain Event Graph, offering a high
degree of flexibility for tailored analyses. For more details on Chain
Event Graphs, see Freeman, G., & Smith, J. Q. (2011)
<doi:10.1016/j.jmva.2011.03.008>, Collazo R. A., Görgen C. and Smith J. Q.
(2018, ISBN:9781498729604) and Barclay, L. M., Hutton, J. L., & Smith, J.
Q. (2014) <doi:10.1214/13-BA843>.

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
