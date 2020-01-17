%global packname  Rsagacmd
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Linking R with the Open-Source 'SAGA-GIS' Software

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         saga >= 2.3.1
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-sf 
Requires:         R-tools 
Requires:         R-CRAN-rgdal 
Requires:         R-foreign 
Requires:         R-CRAN-minpack.lm 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 

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
'raster', 'sp', and 'sf' packages) along with non-spatial data are
automatically passed from R to the 'SAGA-GIS' command line tool for
geoprocessing operations, and the results are loaded as the appropriate R
object. Outputs from individual 'SAGA-GIS' tools can also be chained using
pipes from the 'magrittr' and 'dplyr' packages to combine complex
geoprocessing operations together in a single statement. 'SAGA-GIS' is
available under a GPLv2 / LGPLv2 licence from
<https://sourceforge.net/projects/saga-gis/> including Windows x86/x84
binaries. SAGA-GIS is also included in Debian/Ubuntu default software
repositories and is available for macOS using homebrew
(<https://brew.sh/>) from the osgeo/osgeo4mac
(<https://github.com/OSGeo/homebrew-osgeo4mac>) formula tap. Rsagacmd has
currently been tested on 'SAGA-GIS' versions from 2.3.1 to 7.4.0 on
Windows, Linux and macOS.

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
%{rlibdir}/%{packname}/INDEX
