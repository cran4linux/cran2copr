%global packname  AdhereRViz
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Interactive Visualisation of Medication Adherence Patterns

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.0
BuildRequires:    R-CRAN-RSQLite >= 2.1
BuildRequires:    R-CRAN-haven >= 2.0
BuildRequires:    R-CRAN-data.table >= 1.9
BuildRequires:    R-CRAN-readODS >= 1.6
BuildRequires:    R-CRAN-lubridate >= 1.5
BuildRequires:    R-CRAN-V8 >= 1.5
BuildRequires:    R-CRAN-rsvg >= 1.3
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-readxl >= 1.2
BuildRequires:    R-CRAN-RMariaDB >= 1.0.5
BuildRequires:    R-CRAN-manipulate >= 1.0
BuildRequires:    R-CRAN-shiny >= 1.0
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-colourpicker >= 1.0
BuildRequires:    R-CRAN-DBI >= 1.0
BuildRequires:    R-CRAN-scales >= 1.0
BuildRequires:    R-CRAN-AdhereR >= 0.6
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.4
BuildRequires:    R-CRAN-highlight >= 0.4
BuildRequires:    R-CRAN-clipr >= 0.4
BuildRequires:    R-CRAN-viridisLite >= 0.3
Requires:         R-parallel >= 3.0
Requires:         R-CRAN-RSQLite >= 2.1
Requires:         R-CRAN-haven >= 2.0
Requires:         R-CRAN-data.table >= 1.9
Requires:         R-CRAN-readODS >= 1.6
Requires:         R-CRAN-lubridate >= 1.5
Requires:         R-CRAN-V8 >= 1.5
Requires:         R-CRAN-rsvg >= 1.3
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-readxl >= 1.2
Requires:         R-CRAN-RMariaDB >= 1.0.5
Requires:         R-CRAN-manipulate >= 1.0
Requires:         R-CRAN-shiny >= 1.0
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-colourpicker >= 1.0
Requires:         R-CRAN-DBI >= 1.0
Requires:         R-CRAN-scales >= 1.0
Requires:         R-CRAN-AdhereR >= 0.6
Requires:         R-CRAN-shinyWidgets >= 0.4.4
Requires:         R-CRAN-highlight >= 0.4
Requires:         R-CRAN-clipr >= 0.4
Requires:         R-CRAN-viridisLite >= 0.3

%description
Interactive graphical user interface (GUI) for the package 'AdhereR',
allowing the user to access different data sources, to explore the
patterns of medication use therein, and the computation of various
measures of adherence. It is implemented using Shiny and
HTML/CSS/JavaScript.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/interactivePlotShiny
%{rlibdir}/%{packname}/INDEX
