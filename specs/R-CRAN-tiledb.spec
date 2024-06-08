%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tiledb
%global packver   0.28.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.28.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modern Database Engine for Complex Data Based on Multi-Dimensional Arrays

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    tiledb-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nanotime 
BuildRequires:    R-CRAN-spdl 
BuildRequires:    R-CRAN-nanoarrow 
BuildRequires:    R-CRAN-RcppInt64 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-methods 
Requires:         R-CRAN-nanotime 
Requires:         R-CRAN-spdl 
Requires:         R-CRAN-nanoarrow 

%description
The modern database 'TileDB' introduces a powerful on-disk format for
storing and accessing any complex data based on multi-dimensional arrays.
It supports dense and sparse arrays, dataframes and key-values stores,
cloud storage ('S3', 'GCS', 'Azure'), chunked arrays, multiple
compression, encryption and checksum filters, uses a fully multi-threaded
implementation, supports parallel I/O, data versioning ('time travel'),
metadata and groups. It is implemented as an embeddable cross-platform C++
library with APIs from several languages, and integrations. This package
provides the R support.

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
