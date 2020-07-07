%global packname  csodata
%global packver   1.0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1.1
Release:          3%{?dist}
Summary:          Download Data from the CSO 'StatBank' API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rjstat 
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rjstat 
Requires:         R-CRAN-R.cache 
Requires:         R-CRAN-sf 

%description
Imports 'StatBank' data in JSON-stat format and (optionally) reshapes it
into wide format. The Central Statistics Office (CSO) is the national
statistical institute of Ireland and 'StatBank' is the CSOs online
database of Official Statistics. This database contains current and
historical data series compiled from CSO statistical releases and is
accessed at
<http://www.cso.ie/px/pxeirestat/statire/SelectTable/Omrade0.asp?Planguage=0>.
A tutorial explaining and illustrating how to navigate to the 'StatBank'
and how to search the 'StatBank' by keyword or theme can be found here:
<https://www.cso.ie/en/interactivezone/youtubevideos/statbanktutorial/>.
This tutorial also demonstrates how a user can create, edit and download a
table from the 'StatBank'. The CSO 'StatBank' Application Programming
Interface (API), which is accessed in this package, provides access to
'StatBank' data in JSON-stat format at
<https://statbank.cso.ie/webserviceclient/>. This dissemination tool
allows developers machine to machine access to CSO 'StatBank' data.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
