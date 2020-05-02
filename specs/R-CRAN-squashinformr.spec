%global packname  squashinformr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Politely Web Scrape Data from SquashInfo

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.4.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.2.5
BuildRequires:    R-CRAN-janitor >= 1.2.0
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-naniar >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-rvest >= 0.3.3
BuildRequires:    R-CRAN-polite >= 0.1.1
Requires:         R-CRAN-Hmisc >= 4.4.0
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.2.5
Requires:         R-CRAN-janitor >= 1.2.0
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-naniar >= 0.5.0
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-rvest >= 0.3.3
Requires:         R-CRAN-polite >= 0.1.1

%description
Scrape SquashInfo <http://www.squashinfo.com/> for data on the
Professional Squash Association World Tour and other squash events.
'squashinformr' functions scrape, parse, and clean data associated with
players, tournaments, and rankings.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
