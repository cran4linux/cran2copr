%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TCHazaRds
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tropical Cyclone (Hurricane, Typhoon) Spatial Hazard Modelling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-latticeExtra 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-terra 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ncdf4 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rasterVis 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-latticeExtra 

%description
Methods for generating modelled parametric Tropical Cyclone (TC) spatial
hazard fields and time series output at point locations from TC tracks.
R's compatibility to simply use fast 'cpp' code via the 'Rcpp' package and
the wide range spatial analysis tools via the 'terra' package makes it an
attractive open source environment to study 'TCs'.  This package estimates
TC vortex wind and pressure fields using parametric equations originally
coded up in 'python' by 'TCRM'
<https://github.com/GeoscienceAustralia/tcrm> and then coded up in 'Cuda'
'cpp' by 'TCwindgen' <https://github.com/CyprienBosserelle/TCwindgen>.

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
