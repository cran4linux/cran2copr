%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arcgisgeocode
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Robust Interface to ArcGIS 'Geocoding Services'

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-arcgisutils >= 0.3.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonify 
BuildRequires:    R-CRAN-RcppSimdJson 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-arcgisutils >= 0.3.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonify 
Requires:         R-CRAN-RcppSimdJson 
Requires:         R-CRAN-sf 

%description
A very fast and robust interface to ArcGIS 'Geocoding Services'. Provides
capabilities for reverse geocoding, finding address candidates,
character-by-character search autosuggestion, and batch geocoding. The
public 'ArcGIS World Geocoder' is accessible for free use via
'arcgisgeocode' for all services except batch geocoding. 'arcgisgeocode'
also integrates with 'arcgisutils' to provide access to custom locators or
private 'ArcGIS World Geocoder' hosted on 'ArcGIS Enterprise'. Learn more
in the 'Geocode service' API reference
<https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm>.

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
