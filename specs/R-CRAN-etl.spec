%global packname  etl
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}
Summary:          Extract-Transform-Load Framework for Medium Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DBI 
Requires:         R-datasets 
Requires:         R-CRAN-downloader 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
A predictable and pipeable framework for performing ETL
(extract-transform-load) operations on publicly-accessible medium-sized
data set. This package sets up the method structure and implements generic
functions. Packages that depend on this package download specific data
sets from the Internet, clean them up, and import them into a local or
remote relational database management system.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/sql
%{rlibdir}/%{packname}/INDEX
