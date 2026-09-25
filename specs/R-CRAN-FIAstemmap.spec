%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FIAstemmap
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tree Canopy Modeling for USDA Forest Inventory and Analysis Plots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gdalraster >= 2.5.0
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-stats 
Requires:         R-CRAN-gdalraster >= 2.5.0
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-cli 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-stats 

%description
Maps individual tree stem locations on field plots of the Forest Inventory
and Analysis Program of USDA Forest Service
(<https://research.fs.usda.gov/programs/nfi>). Stem locations are mapped
in cartesian coordinate space based on field-measured distance and azimuth
from subplot and microplot centers. Per-tree crown widths are estimated
using a curated set of allometric equations with coverage for the
conterminous US. Spatial descriptors of tree point pattern are computed at
the whole plot level. Several stand height metrics are also computed and
provided in the output. The spatial representation of modeled tree crowns
is used to generate estimates of fractional tree canopy cover at the
microplot, subplot and whole plot levels. Convenience functions are
provided for efficient data processing. Exploratory data analysis is also
facilitated via integration with the 'spatstat' packages.

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
