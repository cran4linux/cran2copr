%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSAGA
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          SAGA Geoprocessing and Terrain Analysis

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         saga
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-shapefiles 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-shapefiles 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 

%description
Provides access to geocomputing and terrain analysis functions of the
geographical information system (GIS) 'SAGA' (System for Automated
Geoscientific Analyses) from within R by running the command line version
of SAGA. This package furthermore provides several R functions for
handling ASCII grids, including a flexible framework for applying local
functions (including predict methods of fitted models) and focal functions
to multiple grids. SAGA GIS is available under GPL-2 / LGPL-2 licences
from <https://sourceforge.net/projects/saga-gis/>.

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
