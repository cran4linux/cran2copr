%global packname  pointblank
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Validation of Local and Remote Data Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-commonmark >= 1.7
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-rmarkdown >= 1.14
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-RPostgreSQL >= 0.6.2
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-RMySQL >= 0.10.14
BuildRequires:    R-CRAN-messaging >= 0.1.0
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-commonmark >= 1.7
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-rmarkdown >= 1.14
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-RPostgreSQL >= 0.6.2
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-RMySQL >= 0.10.14
Requires:         R-CRAN-messaging >= 0.1.0
Requires:         R-CRAN-magrittr 

%description
Validate data in data frames, 'tibble' objects, in 'CSV' and 'TSV' files,
and in database tables ('PostgreSQL' and 'MySQL'). Validation pipelines
can be made using easily-readable, consecutive validation steps and such
pipelines allow for switching of the data table context. Upon execution of
the validation plan, several reporting options are available. User-defined
thresholds for failure rates allow for the determination of appropriate
reporting actions.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/icons
%doc %{rlibdir}/%{packname}/report_rmd
%{rlibdir}/%{packname}/INDEX
