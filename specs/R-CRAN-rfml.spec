%global packname  rfml
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          MarkLogic NoSQL Database Server in-Database Analytics for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-PKI 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-XML 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-PKI 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-XML 

%description
Functionality required to efficiently use R with MarkLogic NoSQL Database
Server, <http://www.marklogic.com/what-is-marklogic/>. Many basic and
complex R operations are pushed down into the database, which removes the
main memory boundary of R and allows to make full use of MarkLogic server.
In order to use the package you need a MarkLogic Server version 8 or
higher.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ext
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/lib
%{rlibdir}/%{packname}/INDEX
