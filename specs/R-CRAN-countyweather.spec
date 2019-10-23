%global packname  countyweather
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Compiles Meterological Data for U.S. Counties

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggmap >= 2.6.1
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-lubridate >= 1.5.6
BuildRequires:    R-CRAN-geosphere >= 1.5.1
BuildRequires:    R-CRAN-sp >= 1.2.3
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-stringi >= 1.1.1
BuildRequires:    R-CRAN-rnoaa >= 0.6.5
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-tigris >= 0.3.3
BuildRequires:    R-CRAN-tidyr >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.2.1
Requires:         R-CRAN-ggmap >= 2.6.1
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-lubridate >= 1.5.6
Requires:         R-CRAN-geosphere >= 1.5.1
Requires:         R-CRAN-sp >= 1.2.3
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-stringi >= 1.1.1
Requires:         R-CRAN-rnoaa >= 0.6.5
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-tigris >= 0.3.3
Requires:         R-CRAN-tidyr >= 0.3.1
Requires:         R-CRAN-purrr >= 0.2.1

%description
Interacts with NOAA data sources (including the NCDC API at
<http://www.ncdc.noaa.gov/cdo-web/webservices/v2> and ISD data) using
functions from the 'rnoaa' package to obtain and compile weather time
series for U.S. counties. This work was supported in part by grants from
the National Institute of Environmental Health Sciences (R00ES022631) and
the Colorado State University Water Center.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
