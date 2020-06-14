%global packname  dextergui
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          A Graphical User Interface for Dexter

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2
BuildRequires:    R-CRAN-tibble >= 2.1
BuildRequires:    R-CRAN-RCurl >= 1.95
BuildRequires:    R-CRAN-readODS >= 1.6
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.3.0
BuildRequires:    R-CRAN-htmlwidgets >= 1.3
BuildRequires:    R-CRAN-readxl >= 1.1
BuildRequires:    R-CRAN-dexter >= 1.0.2
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-writexl >= 1.0
BuildRequires:    R-CRAN-DT >= 0.9
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-ggExtra >= 0.8
BuildRequires:    R-CRAN-shinyFiles >= 0.7.3
BuildRequires:    R-CRAN-shinyBS >= 0.6
BuildRequires:    R-CRAN-ggridges >= 0.5.1
BuildRequires:    R-CRAN-htmltools >= 0.4.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-networkD3 >= 0.4
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-ggplot2 >= 3.2
Requires:         R-CRAN-tibble >= 2.1
Requires:         R-CRAN-RCurl >= 1.95
Requires:         R-CRAN-readODS >= 1.6
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-shiny >= 1.3.0
Requires:         R-CRAN-htmlwidgets >= 1.3
Requires:         R-CRAN-readxl >= 1.1
Requires:         R-CRAN-dexter >= 1.0.2
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-writexl >= 1.0
Requires:         R-CRAN-DT >= 0.9
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-ggExtra >= 0.8
Requires:         R-CRAN-shinyFiles >= 0.7.3
Requires:         R-CRAN-shinyBS >= 0.6
Requires:         R-CRAN-ggridges >= 0.5.1
Requires:         R-CRAN-htmltools >= 0.4.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-networkD3 >= 0.4
Requires:         R-CRAN-Cairo 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-tools 

%description
Classical Test and Item analysis, Item Response analysis and data
management for educational and psychological tests.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
