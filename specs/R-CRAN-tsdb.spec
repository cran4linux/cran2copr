%global packname  tsdb
%global packver   0.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          2%{?dist}
Summary:          Terribly-Simple Data Base for Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-datetimeutils 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-datetimeutils 
Requires:         R-CRAN-fastmatch 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
A terribly-simple data base for numeric time series, written purely in R,
so no external database-software is needed. Series are stored in
plain-text files (the most-portable and enduring file type) in CSV format.
Timestamps are encoded using R's native numeric representation for
'Date'/'POSIXct', which makes them fast to parse, but keeps them
accessible with other software. The package provides tools for saving and
updating series in this standardised format, for retrieving and joining
data, for summarising files and directories, and for coercing series from
and to other data types (such as 'zoo' series).

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
%doc %{rlibdir}/%{packname}/tests
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
