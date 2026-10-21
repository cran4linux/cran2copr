%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmet
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Read Brazilian Meteorological Data from INMET

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.0
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-curl >= 4.0
Requires:         R-CRAN-jsonlite 

%description
Automates the download and processing of historical hourly weather data
from automatic stations of the Brazilian National Institute of Meteorology
(INMET). It provides the official station catalogue with an offline
snapshot and nearest-station search, validated and resumable downloads
that detect updated archives, and a fast parser for the formatting and
encoding inconsistencies of raw CSV files across years. It returns
analysis-ready data frames with standardized column names and UTC
timestamps. It flags implausible values with transparent quality-control
checks, reports data completeness, and builds daily summaries in each
station's local time with explicit rules for incomplete days. Data are
retrieved from <https://portal.inmet.gov.br/dadoshistoricos> and
<https://apitempo.inmet.gov.br/estacoes/T>.

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
