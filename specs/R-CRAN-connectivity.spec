%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  connectivity
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Resolution Landscape Connectivity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-terra >= 1.8.0
BuildRequires:    R-utils 
Requires:         R-CRAN-terra >= 1.8.0
Requires:         R-utils 

%description
Calculates multi-resolution landscape connectedness, Connected Habitat
(a.k.a. connectivity-adjusted condition), the Protected Area Connectedness
Index (PARC-connectedness) and the Bioclimatic Ecosystem Resilience Index
(BERI) from raster filenames or 'terra' SpatRaster objects. The
multi-resolution method is described in Valavi, R. et al. (2026)
<doi:10.32942/X2S68V>. Uses 'terra' for raster and vector input and
output, input preparation and polygon analysis boundaries, and 'extendr'
to call the 'connectivity-core' 'Rust' numerical engine. Calculations load
the analysis window into memory, and large rasters can be processed as
aligned tiles. Also calculates exact fractional polygon coverage of raster
cells. Bundled example rasters for Tasmania are licensed separately under
CC BY-NC-SA 4.0.

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
