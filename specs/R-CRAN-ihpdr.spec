%global packname  ihpdr
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          Download Data from the International House Price Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-rvest >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-rvest >= 0.3.4
Requires:         R-CRAN-purrr >= 0.3.2

%description
Web scraping the <https://www.dallasfed.org> for up-to-date data on
international house prices and exuberance indicators. Download data in
tidy format.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
