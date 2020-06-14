%global packname  shinyloadtest
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Load Test Shiny Applications

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-httpuv >= 1.5.2
BuildRequires:    R-CRAN-websocket >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-httpuv >= 1.5.2
Requires:         R-CRAN-websocket >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-R6 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-xml2 

%description
Assesses the number of concurrent users 'shiny' applications are capable
of supporting, and for directing application changes in order to support a
higher number of users. Provides facilities for recording 'shiny'
application sessions, playing recorded sessions against a target server at
load, and analyzing the resulting metrics.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/dist
%{rlibdir}/%{packname}/INDEX
