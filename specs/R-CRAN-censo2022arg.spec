%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  censo2022arg
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extraction and Analysis of 2022 Argentina Census Microdata from REDATAM Databases

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-callr >= 3.7.0
BuildRequires:    R-CRAN-redatamx 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-callr >= 3.7.0
Requires:         R-CRAN-redatamx 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-dplyr 

%description
Provides tools to extract, label, and read microdata from the 2022
National Census of Population, Households and Dwellings of Argentina
stored in REDATAM databases officially distributed by INDEC. Implements a
complete province-by-province extraction pipeline with efficient memory
management, reconstruction of hierarchical identifiers, automatic variable
labeling from official INDEC dictionaries, and integrity verification
against published totals. Allows working with census data directly in R
without knowledge of REDATAM syntax, and supports export to multiple
formats including Parquet, CSV, SPSS and SAS. Census data must be
downloaded directly from the official INDEC portal
(<https://www.indec.gob.ar>). This package does not distribute census
data. Duran (2026) <doi:10.5281/zenodo.19560728>.

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
