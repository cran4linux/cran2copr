%global packname  lazyraster
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}%{?buildtag}
Summary:          Generate Raster Data Lazily from 'GDAL'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vapour >= 0.4.0
BuildRequires:    R-CRAN-quadmesh >= 0.4.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
Requires:         R-CRAN-vapour >= 0.4.0
Requires:         R-CRAN-quadmesh >= 0.4.0
Requires:         R-graphics 
Requires:         R-CRAN-raster 
Requires:         R-methods 

%description
Read raster data at a specified resolution on-demand via 'GDAL' (the
Geospatial Data Abstraction Library <https://gdal.org/>). Augments the
'raster' package by never reading data from a raster source until
necessary for generating an in-memory 'raster' object. A 'lazyraster'
object may be cropped and converted to 'raster' object, and by default
will only read a small amount of data sufficient for an overall summary.
The amount of data read can be controlled by specifying the output
dimensions.

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
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/INDEX
