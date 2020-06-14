%global packname  poplite
%global packver   0.99.23
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.23
Release:          2%{?dist}
Summary:          Tools for Simplifying the Population and Querying of SQLiteDatabases

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite >= 2.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-DBI >= 0.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-dbplyr 
Requires:         R-CRAN-RSQLite >= 2.0
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-DBI >= 0.7
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-dbplyr 

%description
Provides objects and accompanying methods which facilitates populating and
querying SQLite databases.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
