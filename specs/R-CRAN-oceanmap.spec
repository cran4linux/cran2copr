%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oceanmap
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          A Plotting Toolbox for 2D Oceanographic Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       ImageMagick
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.9.7
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-mapdata 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggedit 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-sf >= 0.9.7
Requires:         R-CRAN-maps 
Requires:         R-CRAN-mapdata 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-plotrix 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-ncdf4 
Requires:         R-stats 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggedit 
Requires:         R-CRAN-plotly 

%description
Plotting toolbox for 2D oceanographic data (satellite data, sea surface
temperature, chlorophyll, ocean fronts & bathymetry). Recognized classes
and formats include netcdf, Raster, '.nc' and '.gz' files.

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
