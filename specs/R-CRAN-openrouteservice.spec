%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  openrouteservice
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          An 'openrouteservice' API Client

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-jsonvalidate 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-jsonvalidate 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-leaflet 
Requires:         R-utils 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-xml2 

%description
The client streamlines access to the services provided by
<https://api.openrouteservice.org>. It allows you to painlessly query for
directions, isochrones, time-distance matrices, geocoding, elevation,
points of interest, and more.

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
