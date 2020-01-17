%global packname  webmockr
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Stubbing and Setting Expectations on 'HTTP' Requests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.1.3
BuildRequires:    R-CRAN-urltools >= 1.6.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-crul >= 0.7.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-fauxpas 
Requires:         R-CRAN-R6 >= 2.1.3
Requires:         R-CRAN-urltools >= 1.6.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-crul >= 0.7.0
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-fauxpas 

%description
Stubbing and setting expectations on 'HTTP' requests. Includes tools for
stubbing 'HTTP' requests, including expected request conditions and
response conditions. Match on 'HTTP' method, query parameters, request
body, headers and more. Can be used for unit tests or outside of a testing
context.

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
%doc %{rlibdir}/%{packname}/ignore
%{rlibdir}/%{packname}/INDEX
