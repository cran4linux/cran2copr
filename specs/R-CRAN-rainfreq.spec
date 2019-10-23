%global packname  rainfreq
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Rainfall Frequency (Design Storm) Estimates from the US NationalWeather Service

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-SDMTools 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-SDMTools 

%description
Estimates of rainfall at desired frequency (e.g., 1% annual chance or
100-year return period) and desired duration (e.g., 24-hour duration) are
often required in the design of dams and other hydraulic structures,
catastrophe risk modeling, environmental planning and management. One
major source of such estimates for the USA is the NOAA National Weather
Service's (NWS) division of Hydrometeorological Design Studies Center
(HDSC). Raw data from NWS-HDSC is available at 1-km resolution and comes
as a huge number of GIS files. This package provides functionality to
easily access and analyze the 1-km GIS files provided by NWS' PF Data
Server for the entire USA. This package also comes with datasets on record
point rainfall measurements provided by NWS-HDSC.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
