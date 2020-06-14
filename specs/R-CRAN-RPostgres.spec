%global packname  RPostgres
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          'Rcpp' Interface to 'PostgreSQL'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libpq-devel >= 9.0
Requires:         libpq
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-blob >= 1.2.0
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-hms >= 0.5.0
BuildRequires:    R-CRAN-plogr >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.4.2
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-blob >= 1.2.0
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-hms >= 0.5.0
Requires:         R-CRAN-Rcpp >= 0.11.4.2
Requires:         R-CRAN-bit64 
Requires:         R-methods 
Requires:         R-CRAN-withr 

%description
Fully 'DBI'-compliant 'Rcpp'-backed interface to 'PostgreSQL'
<https://www.postgresql.org/>, an open-source relational database.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
