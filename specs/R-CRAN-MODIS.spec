%global packname  MODIS
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}
Summary:          Acquisition and Processing of MODIS Products

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel >= 1.8.0
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mapdata 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mapedit 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ptw 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-mapdata 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-devtools 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-mapedit 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-maptools 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-ptw 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-utils 

%description
Download and processing functionalities for the Moderate Resolution
Imaging Spectroradiometer (MODIS). The package provides automated access
to the global online data archives LP DAAC (<https://lpdaac.usgs.gov/>),
LAADS (<https://ladsweb.modaps.eosdis.nasa.gov/>) and NSIDC
(<https://nsidc.org/>) as well as processing capabilities such as file
conversion, mosaicking, subsetting and time series filtering.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/external
%doc %{rlibdir}/%{packname}/gdal
%{rlibdir}/%{packname}/INDEX
