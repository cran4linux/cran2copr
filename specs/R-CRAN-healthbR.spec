%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  healthbR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access Brazilian Public Health Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-foreign 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-foreign 

%description
Provides easy access to Brazilian public health data from multiple sources
including VIGITEL (Surveillance of Risk Factors for Chronic Diseases by
Telephone Survey), PNS (National Health Survey), 'PNAD' Continua
(Continuous National Household Sample Survey), 'POF' (Household Budget
Survey with food security and consumption data), 'Censo Demografico'
(population denominators via 'SIDRA' API), SIM (Mortality Information
System), SINASC (Live Birth Information System), 'SIH' (Hospital
Information System), 'SIA' (Outpatient Information System), 'SINAN'
(Notifiable Diseases Surveillance), 'CNES' (National Health Facility
Registry), 'SI-PNI' (National Immunization Program - aggregated 1994-2019
via FTP, individual-level 'microdata' 2020+ via 'OpenDataSUS' API),
'SISAB' (Primary Care Health Information System - coverage indicators via
REST API), ANS ('Agencia Nacional de Saude Suplementar' - supplementary
health beneficiaries, consumer complaints, and financial statements),
'ANVISA' ('Agencia Nacional de Vigilancia Sanitaria' - product
registrations, 'pharmacovigilance', 'hemovigilance', 'technovigilance',
and controlled substance sales via 'SNGPC'), and other health information
systems. Data is downloaded from the Brazilian Ministry of Health and
'IBGE' repositories. Data is returned in tidy format following tidyverse
conventions.

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
