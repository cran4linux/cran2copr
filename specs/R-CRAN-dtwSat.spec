%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dtwSat
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Time-Weighted Dynamic Time Warping for Satellite Image Time Series Analysis

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-reshape2 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 

%description
Provides an implementation of the Time-Weighted Dynamic Time Warping
(TWDTW) method for land cover mapping. TWDTW computes the similarity
between satellite image time series with a set of known temporal patterns
(e.g. phenological cycles of the vegetation). 'dtwSat' offers the user
methods to create temporal patterns for land cover types, perform TWDTW
analysis for satellite datasets, visualize the results of the analysis,
produce land cover maps, create temporal plots for land cover change, and
compute accuracy metrics.

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
