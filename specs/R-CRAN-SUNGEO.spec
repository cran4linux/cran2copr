%global packname  SUNGEO
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sub-National Geospatial Data Archive: Geoprocessing Toolkit

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-udunits2 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-cartogram 
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-CRAN-packcircles 
BuildRequires:    R-CRAN-rmapshaper 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-raster 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-udunits2 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-cartogram 
Requires:         R-CRAN-fasterize 
Requires:         R-CRAN-packcircles 
Requires:         R-CRAN-rmapshaper 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rlang 

%description
Tools for integrating spatially-misaligned GIS datasets. Part of the
Sub-National Geospatial Data Archive System
(<https://www.nsf.gov/awardsearch/showAward?AWD_ID=1925693&HistoricalAwards=false>).

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
