%global packname  fitbitViz
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'Fitbit' Visualizations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-varian 
BuildRequires:    R-CRAN-paletteer 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-leafgl 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rayshader 
BuildRequires:    R-CRAN-OpenImageR 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-utils 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-varian 
Requires:         R-CRAN-paletteer 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rstudioapi 
Requires:         R-grDevices 
Requires:         R-CRAN-leafgl 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rayshader 
Requires:         R-CRAN-OpenImageR 
Requires:         R-CRAN-geodist 
Requires:         R-utils 

%description
Connection to the 'Fitbit' Web API by including 'ggplot2' Visualizations,
'Leaflet' and 3-dimensional 'Rayshader' Maps. The 3-dimensional
'Rayshader' Map requires the installation of the 'CopernicusDEM' R package
which includes the 30- and 90-meter elevation data.

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
