%global packname  TSPostgreSQL
%global packver   2015.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2015.4.1
Release:          1%{?dist}
Summary:          'TSdbi' Extensions for 'PostgreSQL'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch
BuildRequires:    R-CRAN-TSdbi >= 2015.1.1
BuildRequires:    R-CRAN-TSsql >= 2015.1.1
BuildRequires:    R-CRAN-DBI >= 0.3.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tframe 
BuildRequires:    R-CRAN-tframePlus 
BuildRequires:    R-CRAN-RPostgreSQL 
Requires:         R-CRAN-TSdbi >= 2015.1.1
Requires:         R-CRAN-TSsql >= 2015.1.1
Requires:         R-CRAN-DBI >= 0.3.1
Requires:         R-methods 
Requires:         R-CRAN-tframe 
Requires:         R-CRAN-tframePlus 
Requires:         R-CRAN-RPostgreSQL 

%description
A 'PostgreSQL' interface for 'TSdbi'. Comprehensive examples of all the
'TS*' packages is provided in the vignette Guide.pdf with the 'TSdata'
package.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/testWithInternet
%doc %{rlibdir}/%{packname}/testWithPostgreSQLserver
%{rlibdir}/%{packname}/INDEX
