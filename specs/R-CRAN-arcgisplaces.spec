%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arcgisplaces
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Search for POIs using ArcGIS 'Places Service'

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-httr2 >= 1.0.5
BuildRequires:    R-CRAN-arcgisutils >= 0.3.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-wk 
Requires:         R-CRAN-httr2 >= 1.0.5
Requires:         R-CRAN-arcgisutils >= 0.3.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-wk 

%description
The ArcGIS 'Places service' is a ready-to-use location service that can
search for businesses and geographic locations around the world. It allows
you to find, locate, and discover detailed information about each place.
Query for places near a point, within a bounding box, filter based on
categories, or provide search text. 'arcgisplaces' integrates with 'sf'
for out of the box compatibility with other spatial libraries. Learn more
in the 'Places service' API reference
<https://developers.arcgis.com/rest/places/>.

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
