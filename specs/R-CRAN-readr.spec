%global packname  readr
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Read Rectangular Text Data

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-hms >= 0.4.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.0.5
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-hms >= 0.4.1
Requires:         R-CRAN-Rcpp >= 0.12.0.5
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-crayon 
Requires:         R-methods 

%description
The goal of 'readr' is to provide a fast and friendly way to read
rectangular data (like 'csv', 'tsv', and 'fwf'). It is designed to
flexibly parse many types of data found in the wild, while still cleanly
failing when data unexpectedly changes.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%doc %{rlibdir}/%{packname}/rcon
