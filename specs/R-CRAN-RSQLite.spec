%global packname  RSQLite
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          2%{?dist}
Summary:          'SQLite' Interface for R

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-blob >= 1.2.0
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-plogr >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgconfig 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-blob >= 1.2.0
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-pkgconfig 

%description
Embeds the 'SQLite' database engine in R and provides an interface
compliant with the 'DBI' package. The source for the 'SQLite' engine is
included.

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
%doc %{rlibdir}/%{packname}/db
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
