%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arcgis
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          ArcGIS Location Services Meta-Package

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-arcgisutils >= 0.3.0
BuildRequires:    R-CRAN-arcgislayers >= 0.2.0
BuildRequires:    R-CRAN-arcgisgeocode >= 0.1.0
BuildRequires:    R-CRAN-arcgisplaces >= 0.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-arcgisutils >= 0.3.0
Requires:         R-CRAN-arcgislayers >= 0.2.0
Requires:         R-CRAN-arcgisgeocode >= 0.1.0
Requires:         R-CRAN-arcgisplaces >= 0.1.0
Requires:         R-CRAN-cli 
Requires:         R-utils 

%description
Provides easy installation and loading of core ArcGIS location services
packages 'arcgislayers', 'arcgisutils', 'arcgisgeocode', and
'arcgisplaces'. Enabling developers to interact with spatial data and
services from 'ArcGIS Online', 'ArcGIS Enterprise', and 'ArcGIS Platform'.
Learn more about the 'arcgis' meta-package at
<https://developers.arcgis.com/r-bridge/>.

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
