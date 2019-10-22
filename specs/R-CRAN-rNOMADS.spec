%global packname  rNOMADS
%global packver   2.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          1%{?dist}
Summary:          An R Interface to the NOAA Operational Model Archive andDistribution System

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 9.0
BuildRequires:    R-CRAN-XML >= 3.98.1.9
BuildRequires:    R-CRAN-GEOmap >= 2.3.5
BuildRequires:    R-CRAN-RCurl >= 1.95.4.7
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-rvest >= 0.3.2
BuildRequires:    R-CRAN-uuid >= 0.1.2
BuildRequires:    R-CRAN-MBA 
Requires:         R-CRAN-fields >= 9.0
Requires:         R-CRAN-XML >= 3.98.1.9
Requires:         R-CRAN-GEOmap >= 2.3.5
Requires:         R-CRAN-RCurl >= 1.95.4.7
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-uuid >= 0.1.2
Requires:         R-CRAN-MBA 

%description
An interface to the National Oceanic and Atmospheric Administration's
Operational Model Archive and Distribution System (NOMADS, see
<http://nomads.ncep.noaa.gov/> for more information) that allows R users
to quickly and efficiently download global and regional weather model data
for processing.  rNOMADS currently supports a variety of models ranging
from global weather data to an altitude of over 40 km, to high resolution
regional weather models, to wave and sea ice models. It can also retrieve
archived NOMADS models.  rNOMADS can retrieve binary data in grib format
as well as import ascii data directly into R by interfacing with the
GrADS-DODS system.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
