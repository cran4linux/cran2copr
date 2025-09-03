%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CDSE
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Copernicus Data Space Ecosystem' API Wrapper

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-lutz 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-geojsonsf 
Requires:         R-grDevices 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-lutz 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
Provides interface to the 'Copernicus Data Space Ecosystem' API
<https://dataspace.copernicus.eu/analyse/apis>, mainly for searching the
catalog of available data from Copernicus Sentinel missions and obtaining
the images for just the area of interest based on selected spectral bands.
The package uses the 'Sentinel Hub' REST API interface
<https://dataspace.copernicus.eu/analyse/apis/sentinel-hub> that provides
access to various satellite imagery archives. It allows you to access raw
satellite data, rendered images, statistical analysis, and other features.
This package is in no way officially related to or endorsed by Copernicus.

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
