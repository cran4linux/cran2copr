%global __brp_check_rpaths %{nil}
%global packname  Rsagacmd
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Linking R with the Open-Source 'SAGA-GIS' Software

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-rvest 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-stars 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-rvest 

%description
Provides an R scripting interface to the open-source 'SAGA-GIS' (System
for Automated Geoscientific Analyses Geographical Information System)
software. 'Rsagacmd' dynamically generates R functions for every
'SAGA-GIS' geoprocessing tool based on the user's currently installed
'SAGA-GIS' version. These functions are contained within an S3 object and
are accessed as a named list of libraries and tools. This structure
facilitates an easier scripting experience by organizing the large number
of 'SAGA-GIS' geoprocessing tools (>700) by their respective library.
Interactive scripting can fully take advantage of code autocompletion
tools (e.g. in 'Rstudio'), allowing for each tools syntax to be quickly
recognized. Furthermore, the most common types of spatial data (via the
'raster', 'terra', 'sp', and 'sf' packages) along with non-spatial data
are automatically passed from R to the 'SAGA-GIS' command line tool for
geoprocessing operations, and the results are loaded as the appropriate R
object. Outputs from individual 'SAGA-GIS' tools can also be chained using
pipes from the 'magrittr' and 'dplyr' packages to combine complex
geoprocessing operations together in a single statement. 'SAGA-GIS' is
available under a GPLv2 / LGPLv2 licence from
<https://sourceforge.net/projects/saga-gis/> including Windows x86/x64
binaries. SAGA-GIS is also included in Debian/Ubuntu default software
repositories and is available for macOS using homebrew
(<https://brew.sh/>) from the osgeo/osgeo4mac
(<https://github.com/OSGeo/homebrew-osgeo4mac>) formula tap, as well as
being bundled within the 'QGIS' application bundle for macOS. Rsagacmd has
currently been tested on 'SAGA-GIS' versions from 2.3.1 to 8.0.1 on
Windows, Linux and macOS.

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
