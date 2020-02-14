%global packname  wallace
%global packver   1.0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6.2
Release:          1%{?dist}
Summary:          A Modular Platform for Reproducible Modeling of Species Nichesand Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.2
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-spocc >= 0.8.0
BuildRequires:    R-CRAN-DT >= 0.4
BuildRequires:    R-CRAN-ENMeval >= 0.3.0
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-spThin 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-leaflet >= 2.0.2
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-spocc >= 0.8.0
Requires:         R-CRAN-DT >= 0.4
Requires:         R-CRAN-ENMeval >= 0.3.0
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-spThin 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-zip 

%description
The 'shiny' application 'wallace' is a modular platform for reproducible
modeling of species niches and distributions. 'wallace' guides users
through a complete analysis, from the acquisition of species occurrence
and environmental data to visualizing model predictions on an interactive
map, thus bundling complex workflows into a single, streamlined interface.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
