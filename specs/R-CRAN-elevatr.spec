%global packname  elevatr
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Access Elevation Data from Various APIs

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-sf 
Requires:         R-methods 

%description
Several web services are available that provide access to elevation data.
This package provides access to several of those services and returns
elevation data either as a SpatialPointsDataFrame from point elevation
services or as a raster object from raster elevation services.  Currently,
the package supports access to the Amazon Web Services Terrain Tiles
<https://registry.opendata.aws/terrain-tiles/>, the Open Topography Global
Datasets API <https://opentopography.org/developers/>, and the USGS
Elevation Point Query Service <https://nationalmap.gov/epqs/>.

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
