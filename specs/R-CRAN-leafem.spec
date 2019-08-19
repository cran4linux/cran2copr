%global packname  leafem
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          'leaflet' Extensions for 'mapview'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.1
BuildRequires:    R-CRAN-htmltools >= 0.3
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-leaflet >= 2.0.1
Requires:         R-CRAN-htmltools >= 0.3
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 

%description
Provides extensions for package 'leaflet', many of which are used by
package 'mapview'. Focus is on functionality readily available in
Geographic Information Systems such as 'Quantum GIS'. Includes functions
to display coordinates of mouse pointer position, query image values via
mouse pointer and zoom-to-layer buttons. Additionally, provides a feature
type agnostic function to add points, lines, polygons to a map.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
