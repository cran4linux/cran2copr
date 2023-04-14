%global __brp_check_rpaths %{nil}
%global packname  mapReasy
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Producing Administrative Boundary Map with Additional FeaturesEmbedded

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-Hmisc 

%description
Produce administrative boundary map, visualize and compare different
factors on map, tracking latitude and longitude, bubble plot. The package
provides some handy functions to produce different administrative maps
easily. Functions to obtain colorful visualization of different regions of
interest and sub-divisional administrative map at different levels are
included. This csn be used to increase feasibility of mapping disease
pattern across different regions (disease mapping) with appropriate colors
having intensity coherent with magnitude of prevalence. In many surveys,
information on location of sample are collected. Sometimes it is of
interest to quick look at the spreadness of the collected sample, check if
any observation falls outside of the survey area and identify them. The
package provides unique function to perform these tasks easily. Besides,
some additional features have been added to make ad-lib comparison of
different factors across the region through these maps. Visual
presentation of two different variables on a particular map using two way
bubble plot is also provided. Simple bar chart and pie chart can be
produced on map to compare several factors.This package will be helpful to
researchers-both statistician and non-statistician, to create geographic
location wise plotting of different indicators. These types of maps are
used in different research areas such public health, economics,
environment, journalism etc. It provides functions that will also be
helpful to users to create map using two indicators at a time (for
example, shade on a map will give the information of one indicator
variable, bar/pie/bubble chart will give the information on another
indicator). Users only need to select the indicator's value and country
wise region specific shapefile and run the functions to find their graphs
quickly.The distinguishable features of the functions in this package are
they are easy to understand to new R users who are searching some ad-lib
functions to produce administrative map with different features and easy
to use for those who are unfamiliar with file format of spatial data or
geographic location data. Functions in this package adopt, compile and
implement functions from some well-known packages on handling spatial data
to make an user friendly functionality. So users do not need any
additional knowledge about spatial statistics or geographic location data.
All the examples presented in this package use shapefile of country
Bangladesh downloaded from <http://www.gadm.org>. Users are requested to
visit <http://www.gadm.org>, then select Download, then choose country and
shapefile from country and File format dropdown menu. After downloading
the shapefile of any particular country as compressed file, unzip the file
and keep them in a known directory or working directory. Shapefiles of
respective countries will be required to produce corresponding country
maps. Use shapefile of corresponding country to produce all types of maps
available in this package.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
