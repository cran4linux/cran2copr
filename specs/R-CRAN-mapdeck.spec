%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mapdeck
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Maps Using 'Mapbox GL JS' and 'Deck.gl'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-geojsonsf >= 2.0.5
BuildRequires:    R-CRAN-jsonify >= 1.2.3
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-googlePolylines >= 0.8.7
BuildRequires:    R-CRAN-sfheaders >= 0.4.5
BuildRequires:    R-CRAN-colourvalues >= 0.3.11
BuildRequires:    R-CRAN-spatialwidget >= 0.2.6
BuildRequires:    R-CRAN-geometries >= 0.2.5
BuildRequires:    R-CRAN-interleave >= 0.1.2
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-rapidjsonr 
Requires:         R-CRAN-geojsonsf >= 2.0.5
Requires:         R-CRAN-jsonify >= 1.2.3
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-googlePolylines >= 0.8.7
Requires:         R-CRAN-sfheaders >= 0.4.5
Requires:         R-CRAN-colourvalues >= 0.3.11
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 

%description
Provides a mechanism to plot an interactive map using 'Mapbox GL'
(<https://docs.mapbox.com/mapbox-gl-js/api/>), a javascript library for
interactive maps, and 'Deck.gl' (<https://deck.gl/>), a javascript library
which uses 'WebGL' for visualising large data sets.

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
