%global packname  leaflet.esri
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          'ESRI' Bindings for the 'leaflet' Package

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.0
BuildRequires:    R-CRAN-leaflet.extras >= 1.0.0
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-leaflet >= 2.0.0
Requires:         R-CRAN-leaflet.extras >= 1.0.0
Requires:         R-CRAN-htmltools 

%description
An add-on package to the 'leaflet' package, which provides bindings for
'ESRI' services. This package allows a user to add 'ESRI' provided
services such as 'MapService', 'ImageMapService', 'TiledMapService' etc.
to a 'leaflet' map.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
