%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spectralR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Obtain and Visualize Spectral Reflectance Data for Earth Surface Polygons

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-rgee >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-sf >= 1.0.7
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-geojsonio >= 0.9.4
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-reshape2 >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-rgee >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-sf >= 1.0.7
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-geojsonio >= 0.9.4

%description
Tools for obtaining, processing, and visualizing spectral reflectance data
for the user-defined land or water surface classes for visual exploring in
which wavelength the classes differ. Input should be a shapefile with
polygons of surface classes (it might be different habitat types, crops,
vegetation, etc.). The Sentinel-2 L2A satellite mission optical bands
pixel data are obtained through the Google Earth Engine service
(<https://earthengine.google.com/>) and used as a source of spectral data.

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
