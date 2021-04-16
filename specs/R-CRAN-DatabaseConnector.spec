%global packname  DatabaseConnector
%global packver   4.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Connecting to Various Database Platforms

License:          Apache License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-SqlRender >= 1.7.0
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-bit64 
Requires:         R-CRAN-SqlRender >= 1.7.0
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-CRAN-rJava 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-bit64 

%description
An R 'DataBase Interface' ('DBI') compatible interface to various database
platforms ('PostgreSQL', 'Oracle', 'Microsoft SQL Server', 'Amazon
Redshift', 'Microsoft Parallel Database Warehouse', 'IBM Netezza', 'Apache
Impala', 'Google BigQuery', and 'SQLite'). Also includes support for
fetching data as 'Andromeda' objects. Uses 'Java Database Connectivity'
('JDBC') to connect to databases (except SQLite).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
