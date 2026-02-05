%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CSHShydRology
%global packver   1.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Canadian Hydrological Analyses

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-tidyhydat 
BuildRequires:    R-CRAN-whitebox 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-MGBT 
BuildRequires:    R-CRAN-outliers 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-Kendall 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggspatial 
Requires:         R-stats 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-tidyhydat 
Requires:         R-CRAN-whitebox 
Requires:         R-datasets 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-MGBT 
Requires:         R-CRAN-outliers 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-Kendall 

%description
A collection of user-submitted functions to aid in the analysis of
hydrological data, particularly for users in Canada. The functions focus
on the use of Canadian data sets, and are suited to Canadian hydrology,
such as the important cold region hydrological processes and will work
with Canadian hydrological models. The functions are grouped into several
themes, currently including Statistical hydrology, Basic data
manipulations, Visualization, and Spatial hydrology. Functions developed
by the Floodnet project are also included. CSHShydRology has been
developed with the assistance of the Canadian Society for Hydrological
Sciences (CSHS) which is an affiliated society of the Canadian Water
Resources Association (CWRA). As of version 1.2.6, functions now fail
gracefully when attempting to download data from a url which is
unavailable.

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
