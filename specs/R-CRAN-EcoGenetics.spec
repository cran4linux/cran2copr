%global packname  EcoGenetics
%global packver   1.2.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1.5
Release:          1%{?dist}
Summary:          Management and Exploratory Analysis of Spatial Data in LandscapeGenetics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-d3heatmap 
BuildRequires:    R-CRAN-edgebundleR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rkt 
BuildRequires:    R-CRAN-SoDA 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-d3heatmap 
Requires:         R-CRAN-edgebundleR 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-party 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rkt 
Requires:         R-CRAN-SoDA 
Requires:         R-CRAN-sp 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Management and exploratory analysis of spatial data in landscape genetics.
Easy integration of information from multiple sources with "ecogen"
objects.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
