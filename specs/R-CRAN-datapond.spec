%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datapond
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Query Curated 'DuckDB' Databases Built from Public Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.0.0
BuildRequires:    R-CRAN-duckdb >= 1.0.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 5.0.0
Requires:         R-CRAN-duckdb >= 1.0.0
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-jsonlite 
Requires:         R-tools 
Requires:         R-utils 

%description
Connects to the 'datapond' registry of curated 'DuckDB' databases built
from public government and research data (immigration courts, campaign
finance, clinical trials, Medicare, and more). Databases are attached
remotely over HTTP so only the byte ranges a query touches are
transferred, or downloaded once for local use. Returns standard 'DBI'
connections that work with 'dbplyr'.

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
