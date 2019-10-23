%global packname  eSDM
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Ensemble Tool for Predictions from Species Distribution Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tmap >= 2.3
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-sf >= 0.6.3
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-dichromat 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-tmap >= 2.3
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-sf >= 0.6.3
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-dichromat 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-lwgeom 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-stats 
Requires:         R-CRAN-units 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-zip 

%description
A tool which allows users to create and evaluate ensembles of species
distribution model (SDM) predictions. Functionality is offered through R
functions or a GUI (R Shiny app). This tool can assist users in
identifying spatial uncertainties and making informed conservation and
management decisions. The package is further described in Woodman et al
(2019) <doi:10.1111/2041-210X.13283>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/eSDM_vignette_helper.R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
