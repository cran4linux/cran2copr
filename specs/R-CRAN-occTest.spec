%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  occTest
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Characterizing and Filtering Species Occurrence Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-biogeo 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-alphahull 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-outliers 
BuildRequires:    R-CRAN-CoordinateCleaner 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-svMisc 
BuildRequires:    R-CRAN-spocc 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-rnaturalearthdata 
BuildRequires:    R-CRAN-pingr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-dataPreparation 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-biogeo 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-alphahull 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-outliers 
Requires:         R-CRAN-CoordinateCleaner 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-svMisc 
Requires:         R-CRAN-spocc 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-rnaturalearthdata 
Requires:         R-CRAN-pingr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-dataPreparation 

%description
Perform multiple tests for potential errors in species occurrence data and
filter, and filter data according to users specifications.

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
