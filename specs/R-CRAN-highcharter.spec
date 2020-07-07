%global packname  highcharter
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          3%{?dist}
Summary:          A Wrapper for the 'Highcharts' Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.1
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-rlang >= 0.1.1
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-tibble >= 1.1
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-rlang >= 0.1.1
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-whisker 

%description
A wrapper for the 'Highcharts' library including shortcut functions to
plot R objects. 'Highcharts' <http://www.highcharts.com/> is a charting
library offering numerous chart types with a simple configuration syntax.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
