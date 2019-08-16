%global packname  leaflet
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Create Interactive Web Maps with the JavaScript 'Leaflet'Library

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-markdown 
Requires:         R-methods 
Requires:         R-CRAN-png 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-stats 

%description
Create and customize interactive maps using the 'Leaflet' JavaScript
library and the 'htmlwidgets' package. These maps can be used directly
from the R console, from 'RStudio', in Shiny applications and R Markdown
documents.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/legacy
%{rlibdir}/%{packname}/INDEX
