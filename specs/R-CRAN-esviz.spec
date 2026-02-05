%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  esviz
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Plotting Functions for Climate Science and Services

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-easyNCDF >= 0.1.4
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-ClimProjDiags 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-s2dv 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-CSTools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-webshot2 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-easyNCDF >= 0.1.4
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-ClimProjDiags 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-s2dv 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-CSTools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-webshot2 
Requires:         R-CRAN-jsonlite 

%description
A plotting package for climate science and services. Provides a set of
functions for visualizing climate data, including maps, time series,
scorecards and other diagnostics. Some functions are adapted and extended
from the 's2dv' and 'CSTools' packages (Manubens et al. (2018)
<doi:10.1016/j.envsoft.2018.01.018>; Pérez-Zanón et al. (2022)
<doi:10.5194/gmd-15-6115-2022>), with more consistent and integrated
functionalities.

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
