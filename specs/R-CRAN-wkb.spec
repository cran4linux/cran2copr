%global packname  wkb
%global packver   0.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Convert Between Spatial Objects and Well-Known Binary Geometry

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-sp 

%description
Utility functions to convert between the 'Spatial' classes specified by
the package 'sp', and the well-known binary '(WKB)' representation for
geometry specified by the Open Geospatial Consortium. Supports 'Spatial'
objects of class 'SpatialPoints', 'SpatialPointsDataFrame',
'SpatialLines', 'SpatialLinesDataFrame', 'SpatialPolygons', and
'SpatialPolygonsDataFrame'. Supports 'WKB' geometry types 'Point',
'LineString', 'Polygon', 'MultiPoint', 'MultiLineString', and
'MultiPolygon'. Includes extensions to enable creation of maps with 'TIBCO
Spotfire'.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
