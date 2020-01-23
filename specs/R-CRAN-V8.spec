%global packname  V8
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}
Summary:          Embedded JavaScript and WebAssembly Engine for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    v8-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-curl >= 1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-curl >= 1.0
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-utils 

%description
An R interface to V8: Google's open source JavaScript and WebAssembly
engine. This package can be compiled either with V8 version 6 and up, a
NodeJS shared library, or the legacy 3.14/3.15 branch of V8.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/wasm
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
