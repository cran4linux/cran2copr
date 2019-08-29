%global packname  dataesgobr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Access and Use Spain Government's API

License:          LGPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinyFiles 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-jsonlite 
Requires:         R-graphics 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinyFiles 

%description
Functions intended to work with the API of the Spain Government
<https://datos.gob.es/en/apidata> that allows you to download, analyze and
generate information through datasets obtained from the API. The API
containing information about multiples topics from the municipalities and
organizations of Spain, it is possible to find URIs corresponding to the
primary sector taxonomy and the identification of geographical coverage
defined in Annexes IV and V
<https://www.boe.es/diario_boe/txt.php?id=BOE-A-2013-2380> (NTI).

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
%{rlibdir}/%{packname}/dataesgobrApp
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/url_params.yml
%{rlibdir}/%{packname}/INDEX
