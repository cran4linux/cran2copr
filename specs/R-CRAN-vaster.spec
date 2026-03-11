%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vaster
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Raster Grid Logic

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Provides raster grid logic, operations that describe a discretized
rectangular domain and do not require access to materialized data. Grids
are arrays with dimension and extent, and many operations are functions of
dimension only: number of columns, number of rows, or they are a
combination of the dimension and the extent the range in x and the range
in y in that order. Here we provide direct access to this logic without
need for connection to any materialized data or formats. Grid logic
includes functions that relate the cell index to row and column, or row
and column to cell index, row, column or cell index to position. These
methods are described in Loudon, TV, Wheeler, JF, Andrew, KP (1980)
<doi:10.1016/0098-3004(80)90015-1>, and implementations were in part
derived from Hijmans R (2024) <doi:10.32614/CRAN.package.terra>.

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
