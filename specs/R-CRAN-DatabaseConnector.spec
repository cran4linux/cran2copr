%global packname  DatabaseConnector
%global packver   2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.2
Release:          1%{?dist}
Summary:          Connecting to Various Database Platforms

License:          Apache License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-SqlRender >= 1.6.3
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-CRAN-ffbase >= 0.12.1
BuildRequires:    R-CRAN-DatabaseConnectorJars 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-bit 
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-urltools 
Requires:         R-CRAN-SqlRender >= 1.6.3
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-CRAN-ffbase >= 0.12.1
Requires:         R-CRAN-DatabaseConnectorJars 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-bit 
Requires:         R-CRAN-ff 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-urltools 

%description
An R 'DataBase Interface' ('DBI') compatible interface to various database
platforms ('PostgreSQL', 'Oracle', 'Microsoft SQL Server', 'Amazon
Redshift', 'Microsoft Parallel Database Warehouse', 'IBM Netezza', 'Apache
Impala', 'Google BigQuery', and 'SQLite'). Also includes support for
fetching data as 'ffdf' objects. Uses 'Java Database Connectivity'
('JDBC') to connect to databases (except SQLite).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/sql
%{rlibdir}/%{packname}/INDEX
