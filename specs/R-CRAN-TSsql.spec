%global packname  TSsql
%global packver   2017.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2017.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Generic SQL Helper Functions for 'TSdbi' SQL Plugins

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tframe >= 2015.1.1
BuildRequires:    R-CRAN-TSdbi >= 2015.1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-tframePlus 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-stats 
Requires:         R-CRAN-tframe >= 2015.1.1
Requires:         R-CRAN-TSdbi >= 2015.1.1
Requires:         R-methods 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-tframePlus 
Requires:         R-CRAN-zoo 
Requires:         R-stats 

%description
Standard SQL query functions used by SQL plugins packages for the 'TSdbi'
interface to time series databases. It will mainly be used by other
packages rather than directly by end users. The one exception is the
function 'TSquery' which can be used to construct a time series from a
database containing observations over time (e.g. balance statements for
multiple years), but where the database is not specifically designed to
store time series (as with other 'TSdbi' SQL plugin packages).
Comprehensive examples of all the 'TS*' packages is provided in the
vignette Guide.pdf with the 'TSdata' package.

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
%doc %{rlibdir}/%{packname}/TSsql
%{rlibdir}/%{packname}/INDEX
