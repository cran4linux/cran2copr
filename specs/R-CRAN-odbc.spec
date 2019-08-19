%global packname  odbc
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Connect to ODBC Compatible Databases (using the DBI Interface)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    unixODBC-devel
Requires:         unixODBC
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-blob >= 1.1.0
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-blob >= 1.1.0
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-methods 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-hms 

%description
A DBI-compatible interface to ODBC databases.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/icons
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
