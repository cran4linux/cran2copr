%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rasterbc
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Access Forest Ecology Layers for British Columbia in 2001-2018

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-sf 
Requires:         R-methods 
Requires:         R-CRAN-terra 

%description
R-based access to a large set of data variables relevant to forest ecology
in British Columbia (BC), Canada. Layers are in raster format at 100m
resolution in the BC Albers projection, hosted at the Federated Research
Data Repository (FRDR) with <doi:10.20383/101.0283>. The collection
includes: elevation; biogeoclimatic zone; wildfire; cutblocks; forest
attributes from Hansen et al. (2013) <doi:10.1139/cjfr-2013-0401> and
Beaudoin et al. (2017) <doi:10.1139/cjfr-2017-0184>; and rasterized Forest
Insect and Disease Survey (FIDS) maps for a number of insect pest species,
all covering the period 2001-2018. Users supply a polygon or point
location in the province of BC, and 'rasterbc' will download the
overlapping raster tiles hosted at FRDR, merging them as needed and
returning the result in R as a 'SpatRaster' object. Metadata associated
with these layers, and code for downloading them from their original
sources can be found in the 'github' repository
<https://github.com/deankoch/rasterbc_src>.

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
