%global packname  rgdal
%global packver   1.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          1%{?dist}
Summary:          Bindings for the 'Geospatial' Data Abstraction Library

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    gdal-devel >= 1.11.4
BuildRequires:    proj-devel >= 4.8.0
Requires:         gdal
Requires:         proj
Requires:         proj-nad
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-sp >= 1.1.0
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-sp >= 1.1.0
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides bindings to the 'Geospatial' Data Abstraction Library ('GDAL')
(>= 1.11.4) and access to projection/transformation operations from the
'PROJ.4' library. The 'GDAL' and 'PROJ.4' libraries are external to the
package, and, when installing the package from source, must be correctly
installed first. From 'rgdal' 1.4.1, provision is made for 'PROJ6'
accommodation, with 'PROJ6' functionality to follow; from 1.4.1 'rgdal'
will build and function when 'PROJ' >= 6. Both 'GDAL' raster and 'OGR'
vector map data can be imported into R, and 'GDAL' raster data and 'OGR'
vector data exported. Use is made of classes defined in the 'sp' package.
Windows and Mac Intel OS X binaries (including 'GDAL', 'PROJ.4' and
'Expat') are provided on 'CRAN'.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/include
%license %{rlibdir}/%{packname}/LICENSE.TXT
%doc %{rlibdir}/%{packname}/m4
%doc %{rlibdir}/%{packname}/OSGeo4W_test
%doc %{rlibdir}/%{packname}/pictures
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/README.windows
%doc %{rlibdir}/%{packname}/SVN_VERSION
%doc %{rlibdir}/%{packname}/vectors
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
