%global packname  protolite
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Highly Optimized Protocol Buffer Serializers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    protobuf-devel
BuildRequires:    protobuf-compiler
Requires:         protobuf
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-jsonlite 

%description
Pure C++ implementations for reading and writing several common data
formats based on Google protocol-buffers. Currently supports 'rexp.proto'
for serialized R objects, 'geobuf.proto' for binary geojson, and
'mvt.proto' for vector tiles. This package uses the auto-generated C++
code by protobuf-compiler, hence the entire serialization is optimized at
compile time. The 'RProtoBuf' package on the other hand uses the protobuf
runtime library to provide a general- purpose toolkit for reading and
writing arbitrary protocol-buffer data in R.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
