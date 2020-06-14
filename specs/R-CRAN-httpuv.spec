%global packname  httpuv
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          2%{?dist}
Summary:          HTTP and WebSocket Server Library

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-later >= 0.8.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-later >= 0.8.0
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-promises 

%description
Provides low-level socket and protocol support for handling HTTP and
WebSocket requests directly from within R. It is primarily intended as a
building block for other packages, rather than making it particularly easy
to create complete web applications using httpuv alone. httpuv is built on
top of the libuv and http-parser C libraries, both of which were developed
by Joyent, Inc. (See LICENSE file for libuv and http-parser license
information.)

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
