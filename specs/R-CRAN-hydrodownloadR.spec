%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hydrodownloadR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Hydrologic Station Catalogs and Time Series from Public APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dataRetrieval 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-ratelimitr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dataRetrieval 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-ratelimitr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-cellranger 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 

%description
Provides a unified, extensible interface to discover hydrologic stations
and download daily time series (e.g., water discharge, water level, water
temperature, and several other water quality parameter) from national and
regional public APIs. Includes a provider registry, S3 generics 'stations'
and 'timeseries', licensing metadata, date-range and 'complete history'
modes, rate limiting and retries, optional authentication via environment
variables, tidy outputs, UTF-8 to ASCII transliteration, and WGS84
coordinates. Designed for reproducible workflows and straightforward
addition of new providers. Background and use cases are described in
Farber et al. (2025) <doi:10.5194/essd-17-4613-2025> and Farber et al.
(2023) <doi:10.57757/IUGG23-2838>.

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
