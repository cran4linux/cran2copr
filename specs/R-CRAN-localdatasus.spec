%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  localdatasus
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Neighborhood-Level Data from Brazil's Unified Health System

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-microdatasus 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-microdatasus 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Retrieves health data from Brazil's Unified Health System (Sistema Único
de Saúde, SUS) at the neighborhood level, with 2022 Census population,
rates per 10,000 inhabitants, coordinates and maps. Simple functions
return deaths, live births, notifiable diseases, hospital admissions,
outpatient consultations, emergency (SAMU) calls and health facilities by
neighborhood, choosing the data source automatically: microdata with the
patient's postal code (CEP), downloaded with the 'microdatasus' package of
Saldanha, Bastos and Barcellos (2019) <doi:10.1590/0102-311x00032419>;
files and open data published by health departments; and regional 'TabNet'
tabulators that tabulate by neighborhood or district. Postal codes and
neighborhood names are linked to the official neighborhoods of the
Brazilian Institute of Geography and Statistics (IBGE) through the
National Address Register for Statistical Purposes (CNEFE) and the 2022
Census tracts, with quality rules for generic postal codes. Function
names, arguments, messages and documentation are in Portuguese, aimed at
Brazilian health researchers.

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
