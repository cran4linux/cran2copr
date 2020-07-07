%global packname  stminsights
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          A 'Shiny' Application for Inspecting Structural Topic Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 1.4.0
BuildRequires:    R-CRAN-stm >= 1.3.3
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-igraph >= 1.2.0
BuildRequires:    R-CRAN-huge >= 1.2.0
BuildRequires:    R-CRAN-tidygraph >= 1.1.0
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-readr >= 1.1.0
BuildRequires:    R-CRAN-ggraph >= 1.0.0
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-ggrepel >= 0.8.0
BuildRequires:    R-CRAN-shinydashboard >= 0.7.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-shinyBS >= 0.6
BuildRequires:    R-CRAN-purrr >= 0.2.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tibble >= 1.4.0
Requires:         R-CRAN-stm >= 1.3.3
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-igraph >= 1.2.0
Requires:         R-CRAN-huge >= 1.2.0
Requires:         R-CRAN-tidygraph >= 1.1.0
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-readr >= 1.1.0
Requires:         R-CRAN-ggraph >= 1.0.0
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-ggrepel >= 0.8.0
Requires:         R-CRAN-shinydashboard >= 0.7.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-shinyBS >= 0.6
Requires:         R-CRAN-purrr >= 0.2.0
Requires:         R-stats 
Requires:         R-CRAN-scales 

%description
This app enables interactive validation, interpretation and visualization
of structural topic models from the 'stm' package by Roberts and others
(2014) <doi:10.1111/ajps.12103>. It also includes helper functions for
model diagnostics and extracting data from effect estimates.

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
%doc %{rlibdir}/%{packname}/app
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
