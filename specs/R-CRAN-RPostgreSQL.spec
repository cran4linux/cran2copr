%global packname  RPostgreSQL
%global packver   0.6-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          R Interface to the 'PostgreSQL' Database System

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildRequires:    R-CRAN-DBI >= 0.3
BuildRequires:    R-methods 
Requires:         R-CRAN-DBI >= 0.3
Requires:         R-methods 

%description
Database interface and 'PostgreSQL' driver for 'R'. This package provides
a Database Interface 'DBI' compliant driver for 'R' to access 'PostgreSQL'
database systems. In order to build and install this package from source,
'PostgreSQL' itself must be present your system to provide 'PostgreSQL'
functionality via its libraries and header files. These files are provided
as 'postgresql-devel' package under some Linux distributions. On 'macOS'
and 'Microsoft Windows' system the attached 'libpq' library source will be
used.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ANNOUNCEMENT
%doc %{rlibdir}/%{packname}/devTests
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
