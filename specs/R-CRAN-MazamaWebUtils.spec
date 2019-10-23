%global packname  MazamaWebUtils
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Utility Functions for Building Web Databrowsers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-webutils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-webutils 

%description
A suite of utility functions providing standardized functionality often
needed in web services including: logging, cache management and parsing of
http request headers.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
