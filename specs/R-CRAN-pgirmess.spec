%global packname  pgirmess
%global packver   1.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.9
Release:          1%{?dist}
Summary:          Spatial Analysis and Data Mining for Field Ecologists

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-splancs >= 2.01.31
BuildRequires:    R-boot >= 1.3.4
BuildRequires:    R-CRAN-sp >= 0.9.97
BuildRequires:    R-CRAN-maptools >= 0.8.36
BuildRequires:    R-CRAN-rgdal >= 0.7.8
BuildRequires:    R-CRAN-spdep >= 0.5.43
BuildRequires:    R-CRAN-rgeos >= 0.3.8
Requires:         R-CRAN-splancs >= 2.01.31
Requires:         R-boot >= 1.3.4
Requires:         R-CRAN-sp >= 0.9.97
Requires:         R-CRAN-maptools >= 0.8.36
Requires:         R-CRAN-rgdal >= 0.7.8
Requires:         R-CRAN-spdep >= 0.5.43
Requires:         R-CRAN-rgeos >= 0.3.8

%description
Set of tools for reading, writing and transforming spatial and seasonal
data in ecology, model selection and specific statistical tests. It
includes functions to discretize polylines into regular point intervals,
link observations to those points, compute geographical coordinates at
regular intervals between waypoints, read subsets of big rasters, compute
zonal statistics or table of categories within polygons or circular
buffers from raster. The package also provides miscellaneous functions for
model selection, spatial statistics, geometries, writing data.frame with
Chinese characters, and some other functions for field ecologists.

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
%{rlibdir}/%{packname}/INDEX
