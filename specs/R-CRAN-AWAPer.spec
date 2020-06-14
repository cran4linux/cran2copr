%global packname  AWAPer
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Catchment Area Weighted Daily Climate Data Anywhere in Australia

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-Evapotranspiration >= 1.14
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-methods 
Requires:         R-CRAN-Evapotranspiration >= 1.14
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-zoo 
Requires:         R-methods 

%description
NetCDF files of the Bureau of Meteorology Australian Water Availability
Project daily national climate grids are built and used for the efficient
extraction of daily point and catchment area weighted precipitation, daily
minimum temperature, daily maximum temperature, vapour pressure deficit,
solar radiation and various measures of evapotranspiration. For details on
the source climate data see <http://www.bom.gov.au/jsp/awap/>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
