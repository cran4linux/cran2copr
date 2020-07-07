%global packname  cmsaf
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}
Summary:          Tools for CM SAF NetCDF Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 9.6
BuildRequires:    R-CRAN-raster >= 2.8
BuildRequires:    R-CRAN-sp >= 1.3
BuildRequires:    R-CRAN-ncdf4 >= 1.16
BuildRequires:    R-CRAN-FNN >= 1.1
BuildRequires:    R-CRAN-rainfarmr >= 0.1
Requires:         R-CRAN-fields >= 9.6
Requires:         R-CRAN-raster >= 2.8
Requires:         R-CRAN-sp >= 1.3
Requires:         R-CRAN-ncdf4 >= 1.16
Requires:         R-CRAN-FNN >= 1.1
Requires:         R-CRAN-rainfarmr >= 0.1

%description
The Satellite Application Facility on Climate Monitoring (CM SAF) is a
ground segment of the European Organization for the Exploitation of
Meteorological Satellites (EUMETSAT) and one of EUMETSATs Satellite
Application Facilities. The CM SAF contributes to the sustainable
monitoring of the climate system by providing essential climate variables
related to the energy and water cycle of the atmosphere
(<http://www.cmsaf.eu>). It is a joint cooperation of eight National
Meteorological and Hydrological Services. The 'cmsaf' R-package provides a
collection of R-operators for the analysis and manipulation of CM SAF
NetCDF formatted data. The 'cmsaf' R-package is tested for CM SAF NetCDF
data. Other CF conform NetCDF data should be applicable, but there is no
guarantee for an error-free application. The 'cmsaf' R-package includes a
'shiny' based interface for an easy application of the 'cmsaf' package
operators and the preparation and visualization of CM SAF NetCDF data. CM
SAF climate data records are provided for free via
(<https://wui.cmsaf.eu>). Detailed information and test data are provided
on the CM SAF webpage (<http://www.cmsaf.eu/R_toolbox>).

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
%doc %{rlibdir}/%{packname}/toolbox
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
