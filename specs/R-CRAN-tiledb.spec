%global packname  tiledb
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}
Summary:          Sparse and Dense Multidimensional Array Storage Engine for DataScience

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-nanotime 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-nanotime 

%description
The data science storage engine 'TileDB' introduces a powerful on-disk
format for multi-dimensional arrays. It supports dense and sparse arrays,
dataframes and key-values stores, cloud storage ('S3', 'GCS', 'Azure'),
chunked arrays, multiple compression, encryption and checksum filters,
uses a fully multi-threaded implementation, supports parallel I/O, data
versioning ('time travel'), metadata and groups. It is implemented as an
embeddable cross-platform C++ library with APIs from several languages,
and integrations.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
