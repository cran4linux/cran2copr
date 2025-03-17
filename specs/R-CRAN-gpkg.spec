%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpkg
%global packver   0.0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.12
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for the Open Geospatial Consortium 'GeoPackage' Format

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DBI 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-DBI 

%description
Build Open Geospatial Consortium 'GeoPackage' files
(<https://www.geopackage.org/>). 'GDAL' utilities for reading and writing
spatial data are provided by the 'terra' package. Additional 'GeoPackage'
and 'SQLite' features for attributes and tabular data are implemented with
the 'RSQLite' package.

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
