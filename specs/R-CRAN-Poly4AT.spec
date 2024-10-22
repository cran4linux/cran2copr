%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Poly4AT
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Access 'INVEKOS' API for Field Polygons

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-readxl 
Requires:         R-utils 

%description
A 'shiny' app that allows to access and use the 'INVEKOS' API for field
polygons in Austria. API documentation is available at
<https://gis.lfrz.gv.at/api/geodata/i009501/ogc/features/v1/>.

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
