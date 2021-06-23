%global __brp_check_rpaths %{nil}
%global packname  PBSmapping
%global packver   2.73.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.73.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mapping Fisheries Data and Spatial Analysis Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
This software has evolved from fisheries research conducted at the Pacific
Biological Station (PBS) in 'Nanaimo', British Columbia, Canada. It
extends the R language to include two-dimensional plotting features
similar to those commonly available in a Geographic Information System
(GIS). Embedded C code speeds algorithms from computational geometry, such
as finding polygons that contain specified point events or converting
between longitude-latitude and Universal Transverse Mercator (UTM)
coordinates. Additionally, we include 'C++' code developed by Angus
Johnson for the 'Clipper' library, data for a global shoreline, and other
data sets in the public domain. Under the user's R library directory
'.libPaths()', specifically in './PBSmapping/doc', a complete user's guide
is offered and should be consulted to use package functions effectively.

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
