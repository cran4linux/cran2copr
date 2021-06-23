%global __brp_check_rpaths %{nil}
%global packname  mapdeck
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Maps Using 'Mapbox GL JS' and 'Deck.gl'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-geojsonsf >= 1.3.3
BuildRequires:    R-CRAN-jsonify >= 1.1.1
BuildRequires:    R-CRAN-googlePolylines >= 0.7.2
BuildRequires:    R-CRAN-colourvalues >= 0.3.4
BuildRequires:    R-CRAN-spatialwidget >= 0.2.3
BuildRequires:    R-CRAN-sfheaders >= 0.2.2
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-geometries 
BuildRequires:    R-CRAN-rapidjsonr 
Requires:         R-CRAN-geojsonsf >= 1.3.3
Requires:         R-CRAN-jsonify >= 1.1.1
Requires:         R-CRAN-googlePolylines >= 0.7.2
Requires:         R-CRAN-colourvalues >= 0.3.4
Requires:         R-CRAN-sfheaders >= 0.2.2
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shiny 

%description
Provides a mechanism to plot an interactive map using 'Mapbox GL'
(<https://docs.mapbox.com/mapbox-gl-js/api/>), a javascript library for
interactive maps, and 'Deck.gl' (<https://deck.gl/>), a javascript library
which uses 'WebGL' for visualising large data sets.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
