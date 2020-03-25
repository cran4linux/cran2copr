%global packname  mapdeck
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
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
BuildRequires:    R-CRAN-spatialwidget >= 0.2.2
BuildRequires:    R-CRAN-sfheaders >= 0.2.1
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-rapidjsonr 
Requires:         R-CRAN-geojsonsf >= 1.3.3
Requires:         R-CRAN-jsonify >= 1.1.1
Requires:         R-CRAN-googlePolylines >= 0.7.2
Requires:         R-CRAN-colourvalues >= 0.3.4
Requires:         R-CRAN-sfheaders >= 0.2.1
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shiny 

%description
Provides a mechanism to plot an interactive map using 'Mapbox GL'
(<https://www.mapbox.com/mapbox-gl-js/api/>), a javascript library for
interactive maps, and 'Deck.gl' (<http://deck.gl/#/>), a javascript
library which uses 'WebGL' for visualising large data sets.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
