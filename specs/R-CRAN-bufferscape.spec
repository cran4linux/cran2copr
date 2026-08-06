%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bufferscape
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Distance-Weighted Landscape Composition in Buffers Around Point Locations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 

%description
Characterises the environment surrounding point locations by computing
land-cover composition within circular buffers directly from vector
polygons, without conversion to a raster grid. For each site and each
class it returns the exact surface area inside the buffer and a
distance-decay weighted "effective" area in which the kernel is integrated
over polygon geometry rather than evaluated at the polygon centroid,
avoiding the large bias the centroid approximation introduces for
elongated features passing close to the site. Polygons may overlap, so
class areas are not constrained to sum to the buffer area. Intended for
buffer-based exposure assessment and fine-scale spatial epidemiology,
where the relevant scale is tens of metres and global land-cover products
are too coarse: land-use regression around air-quality monitors, green
space around residential addresses, vector-surveillance traps, and
comparable designs. The classification dictionary is user-supplied, and
point features and distances to off-buffer reference features are recorded
alongside the areas.

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
