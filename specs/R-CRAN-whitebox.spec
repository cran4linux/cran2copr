%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  whitebox
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          'WhiteboxTools' R Frontend

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
An R frontend for the 'WhiteboxTools' library, which is an advanced
geospatial data analysis platform developed by Prof. John Lindsay at the
University of Guelph's Geomorphometry and Hydrogeomatics Research Group.
'WhiteboxTools' can be used to perform common geographical information
systems (GIS) analysis operations, such as cost-distance analysis,
distance buffering, and raster reclassification. Remote sensing and image
processing tasks include image enhancement (e.g. panchromatic sharpening,
contrast adjustments), image mosaicing, numerous filtering operations,
simple classification (k-means), and common image transformations.
'WhiteboxTools' also contains advanced tooling for spatial hydrological
analysis (e.g. flow-accumulation, watershed delineation, stream network
analysis, sink removal), terrain analysis (e.g. common terrain indices
such as slope, curvatures, wetness index, hillshading; hypsometric
analysis; multi-scale topographic position analysis), and LiDAR data
processing. Suggested citation: Lindsay (2016)
<doi:10.1016/j.cageo.2016.07.003>.

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
