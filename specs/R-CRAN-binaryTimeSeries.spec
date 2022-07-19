%global __brp_check_rpaths %{nil}
%global packname  binaryTimeSeries
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzes a Binary Variable During a Time Series

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-prettymapr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-prettymapr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
A procedure to create maps, pie charts, and stacked bar plots showing the
trajectory of a binary variable during a time series. You provide a time
series of data sets as a stack of raster files or a data frame and call
the various functions in 'binaryTimeSeries' to create your desired
graphics.For more information please consult: Pontius Jr, R. G. (2022).
"Metrics That Make a Difference: How to Analyze Change and Error" Springer
Nature Switzerland AG <doi:10.1007/978-3-030-70765-1> and Bilintoh, T.M.,
(2022). "Intensity Analysis to Study the Dynamics of reforestation in the
Rio Doce Water Basin, Brazil". Frontiers in Remote Sensing, 3 (873341),
13. <doi:10.3389/frsen.2022.873341>.

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
