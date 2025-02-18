%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chillR
%global packver   0.76
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.76
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Phenology Analysis in Temperate Fruit Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ecmwfr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RMAWGEN 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ecmwfr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-keyring 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-metR 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RMAWGEN 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-XML 

%description
The phenology of plants (i.e. the timing of their annual life phases)
depends on climatic cues. For temperate trees and many other plants,
spring phases, such as leaf emergence and flowering, have been found to
result from the effects of both cool (chilling) conditions and heat. Fruit
tree scientists (pomologists) have developed some metrics to quantify
chilling and heat (e.g. see Luedeling (2012)
<doi:10.1016/j.scienta.2012.07.011>). 'chillR' contains functions for
processing temperature records into chilling (Chilling Hours, Utah Chill
Units and Chill Portions) and heat units (Growing Degree Hours). Regarding
chilling metrics, Chill Portions are often considered the most promising,
but they are difficult to calculate. This package makes it easy. 'chillR'
also contains procedures for conducting a PLS analysis relating
phenological dates (e.g. bloom dates) to either mean temperatures or mean
chill and heat accumulation rates, based on long-term weather and
phenology records (Luedeling and Gassner (2012)
<doi:10.1016/j.agrformet.2011.10.020>). As of version 0.65, it also
includes functions for generating weather scenarios with a weather
generator, for conducting climate change analyses for temperature-based
climatic metrics and for plotting results from such analyses. Since
version 0.70, 'chillR' contains a function for interpolating hourly
temperature records.

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
