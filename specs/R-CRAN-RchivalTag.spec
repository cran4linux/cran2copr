%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RchivalTag
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing and Interactive Visualization of Archival Tagging Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-cleangeo 
BuildRequires:    R-CRAN-suntools 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-oceanmap 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggedit 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leaflet.extras2 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-cleangeo 
Requires:         R-CRAN-suntools 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-stringr 
Requires:         R-grDevices 
Requires:         R-CRAN-oceanmap 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggedit 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leaflet.extras2 
Requires:         R-CRAN-sf 

%description
A set of functions to generate, access and analyze standard data products
from archival tagging data.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
