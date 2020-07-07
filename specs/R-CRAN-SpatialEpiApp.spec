%global packname  SpatialEpiApp
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}
Summary:          A Shiny Web Application for the Analysis of Spatial andSpatio-Temporal Disease Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-SpatialEpi 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-SpatialEpi 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-xts 

%description
Runs a Shiny web application that allows to visualize spatial and
spatio-temporal disease data, estimate disease risk and detect clusters.
The application allows to fit Bayesian disease models to obtain risk
estimates and their uncertainty by using the 'R-INLA' package,
<http://www.r-inla.org>, and to detect clusters by using the scan
statistics implemented in 'SaTScan', <https://www.satscan.org>. The
application allows user interaction and creates interactive visualizations
such as maps supporting padding and zooming and tables that allow for
filtering. It also enables the generation of reports containing the
analyses performed.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/SpatialEpiApp
%{rlibdir}/%{packname}/INDEX
