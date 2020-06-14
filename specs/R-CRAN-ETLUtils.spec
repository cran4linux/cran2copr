%global packname  ETLUtils
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          2%{?dist}
Summary:          Utility Functions to Execute Standard Extract/Transform/LoadOperations (using Package 'ff') on Large Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ff >= 2.2.13
BuildRequires:    R-CRAN-bit >= 1.1.12
Requires:         R-CRAN-ff >= 2.2.13
Requires:         R-CRAN-bit >= 1.1.12

%description
Provides functions to facilitate the use of the 'ff' package in
interaction with big data in 'SQL' databases (e.g. in 'Oracle', 'MySQL',
'PostgreSQL', 'Hive') by allowing easy importing directly into 'ffdf'
objects using 'DBI', 'RODBC' and 'RJDBC'. Also contains some basic utility
functions to do fast left outer join merging based on 'match',
factorisation of data and a basic function for re-coding vectors.

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
%doc %{rlibdir}/%{packname}/smalldb.sqlite3
%{rlibdir}/%{packname}/INDEX
