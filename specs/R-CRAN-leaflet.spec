%global packname  leaflet
%global packver   2.0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create Interactive Web Maps with the JavaScript 'Leaflet' Library

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet.providers >= 1.8.0
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
Requires:         R-CRAN-leaflet.providers >= 1.8.0
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

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
