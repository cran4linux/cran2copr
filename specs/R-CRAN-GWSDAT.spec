%global packname  GWSDAT
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          3%{?dist}
Summary:          GroundWater Spatiotemporal Data Analysis Tool (GWSDAT)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-MASS 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-geometry 
Requires:         R-Matrix 
Requires:         R-CRAN-readxl 
Requires:         R-MASS 
Requires:         R-lattice 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-digest 

%description
Shiny application for the analysis of groundwater monitoring data,
designed to work with simple time-series data for solute concentration and
ground water elevation, but can also plot non-aqueous phase liquid (NAPL)
thickness if required. Also provides the import of a site basemap in GIS
shapefile format.

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
%doc %{rlibdir}/%{packname}/application
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
