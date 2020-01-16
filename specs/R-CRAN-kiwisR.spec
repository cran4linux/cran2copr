%global packname  kiwisR
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}
Summary:          A Wrapper for Querying KISTERS 'WISKI' Databases via the 'KiWIS'API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 

%description
A wrapper for querying 'WISKI' databases via the 'KiWIS' 'REST' API.
'WISKI' is an 'SQL' relational database used for the collection and
storage of water data developed by KISTERS and 'KiWIS' is a 'REST' service
that provides access to 'WISKI' databases via HTTP requests
(<https://water.kisters.de/en/technology-trends/kisters-and-open-data/>).
Contains a list of default databases (called 'hubs') and also allows users
to provide their own 'KiWIS' URL. Supports the entire query process- from
metadata to specific time series values. All data is returned as tidy
tibbles.

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
%{rlibdir}/%{packname}/INDEX
