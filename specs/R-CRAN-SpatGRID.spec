%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpatGRID
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Grid Generation from Longitude and Latitude List

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-qpdf 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-qpdf 

%description
The developed function is designed for the generation of spatial grids
based on user-specified longitude and latitude coordinates. The function
first validates the input longitude and latitude values, ensuring they
fall within the appropriate geographic ranges. It then creates a polygon
from the coordinates and determines the appropriate Universal Transverse
Mercator zone based on the provided hemisphere and longitude values.
Subsequently, transforming the input Shapefile to the Universal Transverse
Mercator projection when necessary. Finally, a spatial grid is generated
with the specified interval and saved as a Shapefile. For method details
see, Brus,D.J.(2022).<DOI:10.1201/9781003258940>. The function takes into
account crucial parameters such as the hemisphere (north or south),
desired grid interval, and the output Shapefile path. The developed
function is an efficient tool, simplifying the process of empty spatial
grid generation for applications such as, geo-statistical analysis,
digital soil mapping product generation, etc. Whether for environmental
studies, urban planning, or any other geo-spatial analysis, this package
caters to the diverse needs of users working with spatial data, enhancing
the accessibility and ease of spatial data processing and visualization.

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
