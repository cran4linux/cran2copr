%global packname  gmDatabase
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          2%{?dist}
Summary:          Accessing a Geometallurgical Database with R

License:          GPL (>= 2) | LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RMySQL 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RMySQL 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-shiny 

%description
A template for a geometallurgical database and a fast and easy interface
for accessing it is provided in this package.

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
%doc %{rlibdir}/%{packname}/gmDatabase.sql
%doc %{rlibdir}/%{packname}/startDB.sql
%{rlibdir}/%{packname}/INDEX
