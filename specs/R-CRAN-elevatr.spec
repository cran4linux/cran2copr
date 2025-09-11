%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  elevatr
%global packver   0.99.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.1
Release:          1%{?dist}%{?buildtag}
Summary:          Access Elevation Data from Various APIs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-slippymath 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-units 
Requires:         R-CRAN-slippymath 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-raster 
Requires:         R-methods 

%description
Several web services are available that provide access to elevation data.
This package provides access to many of those services and returns
elevation data either as an 'sf' simple features object from point
elevation services or as a 'raster' object from raster elevation services.
In future versions, 'elevatr' will drop support for 'raster' and will
instead return 'terra' objects. Currently, the package supports access to
the Amazon Web Services Terrain Tiles
<https://registry.opendata.aws/terrain-tiles/>, the Open Topography Global
Datasets API <https://opentopography.org/developers/>, and the USGS
Elevation Point Query Service <https://apps.nationalmap.gov/epqs/>.

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
