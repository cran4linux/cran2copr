%global packname  efts
%global packver   0.9-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          High-Level Functions to Read and Write Ensemble Forecast TimeSeries in netCDF

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7
BuildRequires:    R-CRAN-stringr >= 1.2
BuildRequires:    R-CRAN-ncdf4 >= 1.16
BuildRequires:    R-CRAN-xts >= 0.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-udunits2 
Requires:         R-CRAN-lubridate >= 1.7
Requires:         R-CRAN-stringr >= 1.2
Requires:         R-CRAN-ncdf4 >= 1.16
Requires:         R-CRAN-xts >= 0.10
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-udunits2 

%description
The binary file format 'netCDF' is developed primarily for climate, ocean
and meteorological data, and 'efts' is a package to read and write
Ensemble Forecast Time Series data in 'netCDF'. 'netCDF' has traditionally
been used to store time slices of gridded data, rather than complete time
series of point data. 'efts' facilitates data handling stored in 'netCDF'
files that follow a convention devised in the domain of ensemble
hydrologic forecasting, but possibly applicable in other domains. 'efts'
uses reference class objects to provide a high level interface to read and
write such data, wrapping lower level operations performed using 'ncdf4'.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
