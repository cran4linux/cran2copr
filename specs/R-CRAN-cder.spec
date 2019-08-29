%global packname  cder
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Interface to the California Data Exchange Center

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.3
BuildRequires:    R-CRAN-tibble >= 2.0
BuildRequires:    R-CRAN-lubridate >= 1.7
BuildRequires:    R-CRAN-glue >= 1.3
BuildRequires:    R-CRAN-stringr >= 1.3
BuildRequires:    R-CRAN-readr >= 1.3
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-rlang >= 0.3
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 3.3
Requires:         R-CRAN-tibble >= 2.0
Requires:         R-CRAN-lubridate >= 1.7
Requires:         R-CRAN-glue >= 1.3
Requires:         R-CRAN-stringr >= 1.3
Requires:         R-CRAN-readr >= 1.3
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-rlang >= 0.3
Requires:         R-utils 

%description
Connect to the California Data Exchange Center (CDEC) Web Service
<http://cdec.water.ca.gov/>. 'CDEC' provides a centralized database to
store, process, and exchange real-time hydrologic information gathered by
various cooperators throughout California. The 'CDEC' Web Service
<http://cdec.water.ca.gov/dynamicapp/wsSensorData> provides a data
download service for accessing historical records.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
