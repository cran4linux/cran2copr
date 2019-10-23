%global packname  tidyhydat
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Extract and Tidy Canadian 'Hydrometric' Data

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite >= 2.0
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-dbplyr >= 1.1.0
BuildRequires:    R-CRAN-cli >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-tidyr >= 0.7.1
BuildRequires:    R-CRAN-DBI >= 0.7
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-RSQLite >= 2.0
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-dbplyr >= 1.1.0
Requires:         R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-tidyr >= 0.7.1
Requires:         R-CRAN-DBI >= 0.7
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-rlang >= 0.1.2

%description
Provides functions to access historical and real-time national
'hydrometric' data from Water Survey of Canada data sources
(<http://dd.weather.gc.ca/hydrometric/csv/> and
<http://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/>) and then
applies tidy data principles.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/test_db
%{rlibdir}/%{packname}/INDEX
