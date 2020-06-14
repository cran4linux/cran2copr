%global packname  httptest
%global packver   3.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.0
Release:          2%{?dist}
Summary:          A Test Environment for HTTP Requests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-utils 

%description
Testing and documenting code that communicates with remote servers can be
painful. Dealing with authentication, server state, and other
complications can make testing seem too costly to bother with. But it
doesn't need to be that hard. This package enables one to test all of the
logic on the R sides of the API in your package without requiring access
to the remote service. Importantly, it provides three contexts that mock
the network connection in different ways, as well as testing functions to
assert that HTTP requests were---or were not---made. It also allows one to
safely record real API responses to use as test fixtures. The ability to
save responses and load them offline also enables one to write vignettes
and other dynamic documents that can be distributed without access to a
live server.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
