%global packname  modchart
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          A 'shiny' Module for Creating Charts of Various Types

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rpivotTable 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinydashboardPlus 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sunburstR 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-treemap 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-sparkline 
BuildRequires:    R-CRAN-collapsibleTree 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rpivotTable 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sunburstR 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-treemap 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-sparkline 
Requires:         R-CRAN-collapsibleTree 
Requires:         R-CRAN-plotly 

%description
This is a 'shiny' module that encapsulates various charting options
available in 'htmlwidgets', and provides options for each type of chart, a
'crosstalk' like interface for aggregate reports between 'DT' and other
chart types.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
