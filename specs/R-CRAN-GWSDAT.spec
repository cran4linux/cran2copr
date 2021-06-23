%global __brp_check_rpaths %{nil}
%global packname  GWSDAT
%global packver   3.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          GroundWater Spatiotemporal Data Analysis Tool (GWSDAT)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-zoo 

%description
Shiny application for the analysis of groundwater monitoring data,
designed to work with simple time-series data for solute concentration and
ground water elevation, but can also plot non-aqueous phase liquid (NAPL)
thickness if required. Also provides the import of a site basemap in GIS
shapefile format.

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
