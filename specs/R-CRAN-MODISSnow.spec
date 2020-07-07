%global packname  MODISSnow
%global packver   0.1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.0
Release:          3%{?dist}
Summary:          Provides a Function to Download MODIS Snow Cover

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-gdalUtils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-gdalUtils 

%description
Package for downloading Moderate-resolution Imaging Spectroradiometer
(MODIS) snow cover data. Global daily snow cover at 500 m resolution
derived from MODIS is made available by the National Snow and Ice Center
Data Center <http://nsidc.org/>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
