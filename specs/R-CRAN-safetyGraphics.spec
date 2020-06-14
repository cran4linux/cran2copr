%global packname  safetyGraphics
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Create Interactive Graphics Related to Clinical Trial Safety

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-shinybusy 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-shinybusy 

%description
A framework for evaluation of clinical trial safety. Users can
interactively explore their data using the 'Shiny' application or create
standalone 'htmlwidget' charts. Interactive charts are built using 'd3.js'
and 'webcharts.js' 'JavaScript' libraries.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/safetyGraphics_app
%doc %{rlibdir}/%{packname}/safetyGraphicsHex
%{rlibdir}/%{packname}/INDEX
