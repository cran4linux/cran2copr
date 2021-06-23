%global __brp_check_rpaths %{nil}
%global packname  mapping
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Download, Linking, Manipulating Coordinates for Maps

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-graphics >= 3.6.1
BuildRequires:    R-grid >= 3.6.1
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-mapview >= 2.7.8
BuildRequires:    R-CRAN-tmap >= 2.3.2
BuildRequires:    R-CRAN-cartography >= 2.3.0
BuildRequires:    R-CRAN-leaflet >= 2.0.3
BuildRequires:    R-CRAN-tmaptools >= 2.0.2
BuildRequires:    R-CRAN-jsonlite >= 1.7.1
BuildRequires:    R-CRAN-rgdal >= 1.4.8
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-geojsonio >= 0.9.2
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-sf >= 0.8.1
BuildRequires:    R-CRAN-htmltools >= 0.5.0
BuildRequires:    R-CRAN-viridisLite >= 0.3.0
BuildRequires:    R-CRAN-leafsync >= 0.1.0
BuildRequires:    R-CRAN-leafpop >= 0.0.5
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-curl >= 4.3
Requires:         R-graphics >= 3.6.1
Requires:         R-grid >= 3.6.1
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-mapview >= 2.7.8
Requires:         R-CRAN-tmap >= 2.3.2
Requires:         R-CRAN-cartography >= 2.3.0
Requires:         R-CRAN-leaflet >= 2.0.3
Requires:         R-CRAN-tmaptools >= 2.0.2
Requires:         R-CRAN-jsonlite >= 1.7.1
Requires:         R-CRAN-rgdal >= 1.4.8
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-geojsonio >= 0.9.2
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-sf >= 0.8.1
Requires:         R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-viridisLite >= 0.3.0
Requires:         R-CRAN-leafsync >= 0.1.0
Requires:         R-CRAN-leafpop >= 0.0.5
Requires:         R-utils 
Requires:         R-stats 

%description
Maps are an important tool to visualise variables distribution across
different spatial object. The mapping process require to link the data
with coordinates and then generate the correspondent map. This package
provide coordinates, linking and mapping functions for an automatic,
flexible and easy approach of mapping workflow of different geographical
statistical unit.Geographical coordinates are provided in the package and
automatically linked with the input data to generate maps with internal
provided functions or external functions.provide an easy, flexible and
automatic approach to potentially download updated coordinates, to link
statistical units with coordinates and to aggregate variables based on the
spatial hierarchy of units. The object returned from the package can be
used for thematic maps with the build-in functions provided in mapping or
with other packages already available.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
