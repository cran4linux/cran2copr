%global __brp_check_rpaths %{nil}
%global packname  sf
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Features for R

License:          GPL-2 | MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel >= 2.0.1
BuildRequires:    geos-devel >= 3.4.0
BuildRequires:    proj-devel >= 4.8.0
BuildRequires:    sqlite-devel
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-s2 >= 1.0.7
BuildRequires:    R-CRAN-DBI >= 0.8
BuildRequires:    R-CRAN-units >= 0.6.0
BuildRequires:    R-CRAN-classInt >= 0.4.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-s2 >= 1.0.7
Requires:         R-CRAN-DBI >= 0.8
Requires:         R-CRAN-units >= 0.6.0
Requires:         R-CRAN-classInt >= 0.4.1
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Support for simple features, a standardized way to encode spatial vector
data. Binds to 'GDAL' for reading and writing data, to 'GEOS' for
geometrical operations, and to 'PROJ' for projection conversions and datum
transformations. Uses by default the 's2' package for spherical geometry
operations on ellipsoidal (long/lat) coordinates.

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
