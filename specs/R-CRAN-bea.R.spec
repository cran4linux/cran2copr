%global __brp_check_rpaths %{nil}
%global packname  bea.R
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Bureau of Economic Analysis API

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-googleVis 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-munsell 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-googleVis 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-munsell 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-yaml 

%description
Provides an R interface for the Bureau of Economic Analysis (BEA) API (see
<http://www.bea.gov/API/bea_web_service_api_user_guide.htm> for more
information) that serves two core purposes - 1. To Extract/Transform/Load
data [beaGet()] from the BEA API as R-friendly formats in the user's work
space [transformation done by default in beaGet() can be modified using
optional parameters; see, too, bea2List(), bea2Tab()]. 2. To enable the
search of descriptive meta data [beaSearch()]. Other features of the
library exist mainly as intermediate methods or are in early stages of
development. Important Note - You must have an API key to use this
library. Register for a key at <http://www.bea.gov/API/signup/index.cfm> .

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
