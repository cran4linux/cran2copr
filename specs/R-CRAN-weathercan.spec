%global packname  weathercan
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          3%{?dist}
Summary:          Download Weather Data from the Environment and Climate ChangeCanada Website

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-methods >= 3.2.2
BuildRequires:    R-CRAN-lubridate >= 1.7.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-stringi >= 1.1.2
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.4.1
BuildRequires:    R-CRAN-rvest >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-rlang >= 0.1.4
BuildRequires:    R-CRAN-xml2 >= 0.1.2
Requires:         R-methods >= 3.2.2
Requires:         R-CRAN-lubridate >= 1.7.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-stringi >= 1.1.2
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.4.1
Requires:         R-CRAN-rvest >= 0.3.4
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-rlang >= 0.1.4
Requires:         R-CRAN-xml2 >= 0.1.2

%description
Provides means for downloading historical weather data from the
Environment and Climate Change Canada website
(<http://climate.weather.gc.ca/historical_data/search_historic_data_e.html>).
Data can be downloaded from multiple stations and over large date ranges
and automatically processed into a single dataset. Tools are also provided
to identify stations either by name or proximity to a location.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
