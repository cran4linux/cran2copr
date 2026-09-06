%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datasus
%global packver   0.16.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.1
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface to Brazilian Public Health Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-datasusr >= 0.1.0
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-datasusr >= 0.1.0
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-xml2 

%description
Retrieves public health data from the Department of Informatics
('DATASUS') of the Brazilian Unified Health System ('Sistema Unico de
Saude', 'SUS') through its online tabulation service and open-data
catalog. It covers the Mortality Information System ('SIM'), Live Birth
Information System ('SINASC'), Hospital Information System of the Unified
Health System ('SIH/SUS'), Outpatient Information System of the Unified
Health System ('SIA/SUS'), National Register of Health Establishments
('CNES'), Notifiable Diseases Information System ('SINAN'), National
Immunization Program ('PNI'), Cancer Information System ('SISCAN'), and
Food and Nutrition Surveillance System ('SISVAN'). Contemporary sources
from the 'OpenDataSUS' portal include Events Supposedly Attributable to
Vaccination or Immunization ('ESAVI'), influenza-like illness
notifications from 'e-SUS Notifica', individual vaccination doses,
coronavirus disease 2019 (COVID-19) hospital occupancy, and record-level
mortality, live-birth and hospital-admission microdata. Curated schemas,
selective columns, multipart downloads and chunk processing support
memory-efficient analysis of large files. The package also provides
grouped epidemiological indicators, confidence intervals,
population-denominator joins, epidemiological calendars, moving averages
and direct age standardization. An offline reference from the Brazilian
Institute of Geography and Statistics (IBGE) supports territorial codes,
joins and completion of geographic time series.

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
