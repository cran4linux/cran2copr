%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AirMonitor
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Air Quality Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-MazamaCoreUtils >= 0.5.3
BuildRequires:    R-CRAN-MazamaTimeSeries >= 0.3.1
BuildRequires:    R-CRAN-MazamaRollUtils >= 0.1.4
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-MazamaCoreUtils >= 0.5.3
Requires:         R-CRAN-MazamaTimeSeries >= 0.3.1
Requires:         R-CRAN-MazamaRollUtils >= 0.1.4
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-xts 

%description
Utilities for working with hourly air quality monitoring data with a focus
on small particulates (PM2.5). A compact data model is structured as a
list with two dataframes. A 'meta' dataframe contains spatial and
measuring device metadata associated with deployments at known locations.
A 'data' dataframe contains a 'datetime' column followed by columns of
measurements associated with each "device-deployment". Algorithms to
calculate NowCast and the associated Air Quality Index (AQI) are defined
at the US Environmental Projection Agency AirNow program:
<https://document.airnow.gov/technical-assistance-document-for-the-reporting-of-daily-air-quailty.pdf>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
