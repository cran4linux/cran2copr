%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pacu
%global packver   0.1.44
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.44
Release:          1%{?dist}%{?buildtag}
Summary:          Precision Agriculture Computational Utilities

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-apsimx 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-concaveman 
BuildRequires:    R-CRAN-tmap 
Requires:         R-CRAN-apsimx 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-units 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-concaveman 
Requires:         R-CRAN-tmap 

%description
Support for a variety of commonly used precision agriculture operations.
Includes functions to download and process raw satellite images from
Sentinel-2
<https://documentation.dataspace.copernicus.eu/APIs/OData.html>. Includes
functions that download vegetation index statistics for a given period of
time, without the need to download the raw images
<https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Statistical.html>.
There are also functions to download and visualize weather data in a
historical context. Lastly, the package also contains functions to process
yield monitor data. These functions can build polygons around recorded
data points, evaluate the overlap between polygons, clean yield data, and
smooth yield maps.

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
