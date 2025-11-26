%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BLSloadR
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Download Time Series Data from the U.S. Bureau of Labor Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tigris >= 2.0
BuildRequires:    R-CRAN-lubridate >= 1.9
BuildRequires:    R-CRAN-zoo >= 1.8
BuildRequires:    R-CRAN-stringr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.7
BuildRequires:    R-CRAN-readxl >= 1.4.5
BuildRequires:    R-CRAN-tidyselect >= 1.2
BuildRequires:    R-CRAN-data.table >= 1.16
BuildRequires:    R-CRAN-dplyr >= 1.1
BuildRequires:    R-CRAN-rvest >= 1.0.4
BuildRequires:    R-CRAN-sf >= 1.0
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-tigris >= 2.0
Requires:         R-CRAN-lubridate >= 1.9
Requires:         R-CRAN-zoo >= 1.8
Requires:         R-CRAN-stringr >= 1.5
Requires:         R-CRAN-httr >= 1.4.7
Requires:         R-CRAN-readxl >= 1.4.5
Requires:         R-CRAN-tidyselect >= 1.2
Requires:         R-CRAN-data.table >= 1.16
Requires:         R-CRAN-dplyr >= 1.1
Requires:         R-CRAN-rvest >= 1.0.4
Requires:         R-CRAN-sf >= 1.0
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rstudioapi 

%description
These functions provide a convenient interface for downloading data from
the U.S. Bureau of Labor Statistics <https://www.bls.gov>.  The functions
in this package utilize flat files produced by the Bureau of Labor
Statistics, which contain full series history.  These files include
employment, unemployment, wages, prices, industry and occupational data at
a national, state, and sub-state level, depending on the series.
Individual functions are included for those programs which have data
available at the state level.  The core functions provide direct access to
the Current Employment Statistics (CES) <https://www.bls.gov/ces/>, Local
Area Unemployment Statistics (LAUS) <https://www.bls.gov/lau/>,
Occupational Employment and Wage Statistics (OEWS)
<https://www.bls.gov/oes/> and Alternative Measures of Labor
Underutilization (SALT) <https://www.bls.gov/lau/stalt.htm> data produced
by the Bureau of Labor Statistics.

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
