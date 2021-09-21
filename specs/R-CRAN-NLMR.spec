%global __brp_check_rpaths %{nil}
%global packname  NLMR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Neutral Landscape Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-spatstat.core 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-spatstat.core 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-igraph 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-fasterize 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Rcpp 

%description
Provides neutral landscape models (<doi:10.1007/BF02275262>,
<http://sci-hub.tw/10.1007/bf02275262>). Neutral landscape models range
from "hard" neutral models (completely random distributed), to "soft"
neutral models (definable spatial characteristics) and generate landscape
patterns that are independent of ecological processes. Thus, these
patterns can be used as null models in landscape ecology. 'NLMR' combines
a large number of algorithms from other published software for simulating
neutral landscapes. The simulation results are obtained in a spatial data
format (raster* objects from the 'raster' package) and can, therefore, be
used in any sort of raster data operation that is performed with standard
observation data.

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
