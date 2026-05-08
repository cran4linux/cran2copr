%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  toro
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive & Customisable Maps using the 'MapLibre GL JS' Library

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-sf 

%description
Create interactive maps that can keep up with complex visualisations and
large datasets, with this useful interface to the 'MapLibre GL JS'
(<https://maplibre.org/maplibre-gl-js/docs/>) library. Users can create
maps directly in the console, or as an HTML widget within 'Shiny' web
applications, and render spatial data quickly with many customisable
options (clusters, custom icons, map layers, and backgrounds). The goal of
the package is to make it easier to interpret and explore large spatial
datasets within the context of a 'Shiny' dashboard, without having long
loading times waiting for a map to update with new data.

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
