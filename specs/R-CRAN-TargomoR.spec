%global packname  TargomoR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Interface to the 'Targomo' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-xml2 

%description
Functions to provide an intuitive interface for retrieving travel time
data from the 'Targomo' API (see <https://targomo.com/developers/> for
details). Provides support for retrieving isochrone polygons, travel
routes, times and distances. Also includes functions for easily adding the
data to 'leaflet' maps, and functions for using the 'Targomo' map tiles.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
