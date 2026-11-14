%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  duckdf
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          SQL for Dataframes, but with Ducks

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-duckdb >= 1.5.6
BuildRequires:    R-CRAN-DBI >= 1.1.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-duckdb >= 1.5.6
Requires:         R-CRAN-DBI >= 1.1.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-jsonlite 

%description
An SQL interface for R dataframes built on the DuckDB embedded analytical
database. Dataframes are registered directly with an in-process DuckDB
instance and queried with standard SQL, so analyses can join, filter,
aggregate and reshape R objects with SQL while results are returned as
dataframes, without copying data to an external database server. The
package wraps the 'duckdb' R package with a DBI-compliant connection and
provides a small, checked surface for the common
register-query-unnregister workflow. The underlying engine and its
vectorised execution model are described in Raasveldt and Mühleisen (2019)
<doi:10.1145/3299869.3320212>.

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
