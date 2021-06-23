%global __brp_check_rpaths %{nil}
%global packname  routr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Simple Router for HTTP and WebSocket Requests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reqres 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-uuid 
Requires:         R-utils 
Requires:         R-CRAN-reqres 
Requires:         R-CRAN-stringi 
Requires:         R-tools 
Requires:         R-CRAN-digest 

%description
In order to make sure that web request ends up in the correct handler
function a router is often used. 'routr' is a package implementing a
simple but powerful routing functionality for R based servers. It is a
fully functional 'fiery' plugin, but can also be used with other 'httpuv'
based servers.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
