%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quak
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Query 'Azure Data Lake Storage Gen2' with 'DuckDB'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-duckdb 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-duckdb 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rlang 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides convenience utilities for using 'DuckDB' directly over datasets
stored in 'Azure Data Lake Storage Gen2' (ADLS Gen2, 'abfss://'). Opens
connections configured for Azure-backed 'Delta Lake' and 'Parquet' data,
registers Azure credentials as 'DuckDB' secrets, and supports optional
repository mirrors for restricted networks. Integrates well with 'DBI' for
SQL workflows and with 'dplyr' and 'dbplyr' for lazy table queries.

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
