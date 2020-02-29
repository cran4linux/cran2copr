%global packname  uavRmp
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}
Summary:          UAV Mission Planner

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-log4r 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-spatial.tools 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-brew 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-geosphere 
Requires:         R-tools 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-log4r 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-spatial.tools 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-roxygen2 
Requires:         R-methods 
Requires:         R-CRAN-brew 

%description
The Unmanned Aerial Vehicle Mission Planner provides an easy to use work
flow for planning autonomous obstacle avoiding surveys of (almost) ready
to fly unmanned aerial vehicles to retrieve aerial or spot related data.
It creates either intermediate flight control files for the DJI phantom
series or ready to upload control files for the pixhawk based flight
controller as used in the 3DR Solo. Additionally it contains some useful
tools for digitizing and data manipulation.

%prep
%setup -q -c -n %{packname}
find %{packname}/{python,htmlwidgets} -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \;
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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/python
%{rlibdir}/%{packname}/INDEX
