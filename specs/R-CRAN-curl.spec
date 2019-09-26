%global packname  curl
%global packver   4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2
Release:          1%{?dist}
Summary:          A Modern and Flexible Web Client for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libcurl-devel
Requires:         libcurl
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
The curl() and curl_download() functions provide highly configurable
drop-in replacements for base url() and download.file() with better
performance, support for encryption (https, ftps), gzip compression,
authentication, and other 'libcurl' goodies. The core of the package
implements a framework for performing fully customized requests where data
can be processed either in memory, on disk, or streaming via the callback
or connection interfaces. Some knowledge of 'libcurl' is recommended; for
a more-user-friendly web client see the 'httr' package which builds on
this package with http specific tools and logic.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
