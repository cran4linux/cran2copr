%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deckglgeoarrow
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Use 'GeoArrow' to Add 'Deck.gl' Layers to a 'maplibregl'/'mapboxgl' Map

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geoarrow 
BuildRequires:    R-CRAN-geoarrowWidget 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-nanoarrow 
Requires:         R-CRAN-geoarrow 
Requires:         R-CRAN-geoarrowWidget 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-nanoarrow 

%description
Leverages the high-performance 'GeoArrow' memory layout to render
potentially very large 'Deck.gl' data layers on a 'maplibregl'/'mapboxgl'
map created with R package 'mapgl'. The heavy lifting is done on the
'JavaScript' side in the browser using 'deck.gl-geoarrow'
(<https://github.com/geoarrow/deck.gl-geoarrow/>). Currently provides
functions for adding Scatterplot (points), Path (lines) and Polygon
(polygons) layers. Has support for data classes from R packages 'wk' and
'sf'. In addition, convenience functions for styling data, tooltips and
popups, as well as layer management are provided. Furthermore, remotely
hosted 'GeoParquet' and 'GeoArrow' files can be visualised directly in the
browser, without the need to first read them into R memory. Only the
styling instructions are prepared by the user in R and are then
transferred to and applied in the browser as the data arrives.

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
