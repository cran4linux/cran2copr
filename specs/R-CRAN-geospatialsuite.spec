%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geospatialsuite
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Geospatiotemporal Analysis and Multimodal Integration Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tigris 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mice 
Requires:         R-parallel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tigris 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-viridis 

%description
A comprehensive toolkit for geospatiotemporal analysis featuring 60+
vegetation indices, advanced raster visualization, universal spatial
mapping, water quality analysis, CDL crop analysis, spatial interpolation,
temporal analysis, and terrain analysis. Designed for agricultural
research, environmental monitoring, remote sensing applications, and
publication-quality mapping with support for any geographic region and
robust error handling. Methods include vegetation indices calculations
(Rouse et al. 1974), NDVI and enhanced vegetation indices (Huete et al.
1997) <doi:10.1016/S0034-4257(97)00104-1>, spatial interpolation
techniques (Cressie 1993, ISBN:9780471002556), water quality indices
(McFeeters 1996) <doi:10.1080/01431169608948714>, and crop data layer
analysis (USDA NASS 2024)
<https://www.nass.usda.gov/Research_and_Science/Cropland/>.  Funding: This
material is based upon financial support by the National Science
Foundation, EEC Division of Engineering Education and Centers, NSF
Engineering Research Center for Advancing Sustainable and Distributed
Fertilizer production (CASFER), NSF 20-553 Gen-4 Engineering Research
Centers award 2133576.

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
