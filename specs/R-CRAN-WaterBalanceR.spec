%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WaterBalanceR
%global packver   0.1.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.19
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate High Resolution Water Balance of Starch Potatoes

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rdwd 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-RSelenium 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-openeo 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rdwd 
Requires:         R-utils 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-RSelenium 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-RCurl 
Requires:         R-grDevices 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-openeo 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-scales 
Requires:         R-methods 
Requires:         R-CRAN-rlang 

%description
Calculates the water balance of starch potatoes from Normalized Distance
Vegetation Index (NDVI) images, German Weather Service (DWD) reference
evapotranspiration, German Weather Service RADOLAN precipitation data and
irrigation information. For more details see Piernicke et al. (2025)
<doi:10.3390/rs17183227>.

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
