%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dbProject
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Database Connection Management and Utilities for 'dbverse'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-duckdb >= 1.4.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-pins 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-connections 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-duckdb >= 1.4.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-pins 
Requires:         R-CRAN-dbplyr 
Requires:         R-methods 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-connections 
Requires:         R-CRAN-yaml 

%description
Provides an R6-based project container for managing 'DuckDB' connections,
reconnecting lazy database tables after session restarts, and storing
metadata for database-backed objects used by packages in the 'dbverse'.
The package supplies S4 base classes and generics for database-backed
data, helpers for validating 'DuckDB' connections and table names,
utilities for creating persistent database views, and methods for writing
and restoring pinned lazy tables through the 'pins' package. These tools
help package authors and analysts keep database paths, cached connections,
and table references synchronized across interactive sessions and project
directories.

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
