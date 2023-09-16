%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cmsaf
%global packver   3.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolbox for CM SAF NetCDF Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-tcltk >= 3.5
BuildRequires:    R-CRAN-maps >= 3.3
BuildRequires:    R-CRAN-raster >= 3.0
BuildRequires:    R-CRAN-R.utils >= 2.9
BuildRequires:    R-CRAN-colorspace >= 1.4
BuildRequires:    R-CRAN-shiny >= 1.4
BuildRequires:    R-CRAN-cmsafops >= 1.2.0
BuildRequires:    R-CRAN-ncdf4 >= 1.17
BuildRequires:    R-CRAN-cmsafvis >= 1.1.5
BuildRequires:    R-CRAN-FNN >= 1.1
BuildRequires:    R-CRAN-shinyjs >= 1.1
BuildRequires:    R-CRAN-shinythemes >= 1.1
BuildRequires:    R-CRAN-colourpicker >= 1.0
BuildRequires:    R-CRAN-shinyFiles >= 0.8.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.6
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-SearchTrees 
BuildRequires:    R-CRAN-xml2 
Requires:         R-tcltk >= 3.5
Requires:         R-CRAN-maps >= 3.3
Requires:         R-CRAN-raster >= 3.0
Requires:         R-CRAN-R.utils >= 2.9
Requires:         R-CRAN-colorspace >= 1.4
Requires:         R-CRAN-shiny >= 1.4
Requires:         R-CRAN-cmsafops >= 1.2.0
Requires:         R-CRAN-ncdf4 >= 1.17
Requires:         R-CRAN-cmsafvis >= 1.1.5
Requires:         R-CRAN-FNN >= 1.1
Requires:         R-CRAN-shinyjs >= 1.1
Requires:         R-CRAN-shinythemes >= 1.1
Requires:         R-CRAN-colourpicker >= 1.0
Requires:         R-CRAN-shinyFiles >= 0.8.0
Requires:         R-CRAN-shinyWidgets >= 0.6
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-SearchTrees 
Requires:         R-CRAN-xml2 

%description
The Satellite Application Facility on Climate Monitoring (CM SAF) is a
ground segment of the European Organization for the Exploitation of
Meteorological Satellites (EUMETSAT) and one of EUMETSATs Satellite
Application Facilities. The CM SAF contributes to the sustainable
monitoring of the climate system by providing essential climate variables
related to the energy and water cycle of the atmosphere
(<https://www.cmsaf.eu>). It is a joint cooperation of eight National
Meteorological and Hydrological Services. The 'cmsaf' R-package includes a
'shiny' based interface for an easy application of the 'cmsafops' and
'cmsafvis' packages - the CM SAF R Toolbox. The Toolbox offers an easy way
to prepare, manipulate, analyse and visualize CM SAF NetCDF formatted
data. Other CF conform NetCDF data with time, longitude and latitude
dimension should be applicable, but there is no guarantee for an
error-free application. CM SAF climate data records are provided for free
via (<https://wui.cmsaf.eu/safira>). Detailed information and test data
are provided on the CM SAF webpage (<http://www.cmsaf.eu/R_toolbox>).

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
