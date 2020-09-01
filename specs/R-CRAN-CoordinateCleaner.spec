%global packname  CoordinateCleaner
%global packver   2.0-17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.17
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Cleaning of Occurrence Records from BiologicalCollections

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel >= 2.0.1
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
Automated flagging of common spatial and temporal errors in biological and
paleontological collection data, for the use in conservation, ecology and
paleontology. Includes automated tests to easily flag (and exclude)
records assigned to country or province centroid, the open ocean, the
headquarters of the Global Biodiversity Information Facility, urban areas
or the location of biodiversity institutions (museums, zoos, botanical
gardens, universities). Furthermore identifies per species outlier
coordinates, zero coordinates, identical latitude/longitude and invalid
coordinates. Also implements an algorithm to identify data sets with a
significant proportion of rounded coordinates. Especially suited for large
data sets. The reference for the methodology is: Zizka et al. (2019)
doi:10.1111/2041-210X.13152.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
