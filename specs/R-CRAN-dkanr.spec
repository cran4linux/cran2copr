%global packname  dkanr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Client for the 'DKAN' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-assertthat >= 0.2.0

%description
Provides functions to facilitate access to the 'DKAN' API
(<https://dkan.readthedocs.io/en/latest/apis/index.html>), including the
'DKAN' REST API (metadata), and the 'DKAN' datastore API (data). Includes
functions to list, create, retrieve, update, and delete datasets and
resources nodes. It also includes functions to search and retrieve data
from the 'DKAN' datastore.

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
%doc %{rlibdir}/%{packname}/NOTICE.md
%{rlibdir}/%{packname}/INDEX
