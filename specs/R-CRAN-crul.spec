%global packname  crul
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          HTTP Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.3
BuildRequires:    R-CRAN-R6 >= 2.2.0
BuildRequires:    R-CRAN-urltools >= 1.6.0
BuildRequires:    R-CRAN-httpcode >= 0.2.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mime 
Requires:         R-CRAN-curl >= 3.3
Requires:         R-CRAN-R6 >= 2.2.0
Requires:         R-CRAN-urltools >= 1.6.0
Requires:         R-CRAN-httpcode >= 0.2.0
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mime 

%description
A simple HTTP client, with tools for making HTTP requests, and mocking
HTTP requests. The package is built on R6, and takes inspiration from
Ruby's 'faraday' gem (<https://rubygems.org/gems/faraday>). The package
name is a play on curl, the widely used command line tool for HTTP, and
this package is built on top of the R package 'curl', an interface to
'libcurl' (<https://curl.haxx.se/libcurl>).

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
