%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MazamaTimeSeries
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Core Functionality for Environmental Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MazamaCoreUtils >= 0.4.10
BuildRequires:    R-CRAN-MazamaRollUtils >= 0.1.3
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-MazamaCoreUtils >= 0.4.10
Requires:         R-CRAN-MazamaRollUtils >= 0.1.3
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 

%description
Utility functions for working with environmental time series data from
known locations. The compact data model is structured as a list with two
dataframes. A 'meta' dataframe contains spatial and measuring device
metadata associated with deployments at known locations. A 'data'
dataframe contains a 'datetime' column followed by columns of measurements
associated with each "device-deployment". Ephemerides calculations are
based on code originally found in NOAA's "Solar Calculator"
<https://gml.noaa.gov/grad/solcalc/>.

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
