%global packname  pointblank
%global packver   0.3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1.1
Release:          2%{?dist}
Summary:          Validation of Local and Remote Data Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-cli >= 2.0.2
BuildRequires:    R-CRAN-dbplyr >= 1.4.2
BuildRequires:    R-CRAN-glue >= 1.3.2
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-htmltools >= 0.4.0
BuildRequires:    R-CRAN-blastula >= 0.3.1
BuildRequires:    R-CRAN-ggforce >= 0.3.1
BuildRequires:    R-CRAN-gt >= 0.2.0.5
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-cli >= 2.0.2
Requires:         R-CRAN-dbplyr >= 1.4.2
Requires:         R-CRAN-glue >= 1.3.2
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-htmltools >= 0.4.0
Requires:         R-CRAN-blastula >= 0.3.1
Requires:         R-CRAN-ggforce >= 0.3.1
Requires:         R-CRAN-gt >= 0.2.0.5
Requires:         R-CRAN-magrittr 

%description
Validate data in data frames, 'tibble' objects, and in database tables
(e.g., 'PostgreSQL' and 'MySQL'). Validation pipelines can be made using
easily-readable, consecutive validation steps. Upon execution of the
validation plan, several reporting options are available. User-defined
thresholds for failure rates allow for the determination of appropriate
reporting actions.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/css
%{rlibdir}/%{packname}/javascript
%doc %{rlibdir}/%{packname}/lib
%doc %{rlibdir}/%{packname}/small_table.db
%{rlibdir}/%{packname}/INDEX
