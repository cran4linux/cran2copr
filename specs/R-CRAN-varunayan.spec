%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  varunayan
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Process 'ERA5', IMD, 'HadEX3' and 'CRU TS' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ecmwfr >= 2.0.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ecmwfr >= 2.0.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-parallel 

%description
Download climate data for a bounding box, polygon or point and return tidy
tables. Sources are the 'ERA5' reanalysis (Hersbach et al. (2020)
<doi:10.1002/qj.3803>) from the 'Copernicus' Climate Data Store
<https://cds.climate.copernicus.eu/>, India Meteorological Department
(IMD) gridded rainfall and temperature (Pai et al. (2014)
<doi:10.54302/mausam.v65i1.851>), 'HadEX3' climate extremes (Dunn et al.
(2020) <doi:10.1029/2019JD032263>) and 'CRU TS' (Harris et al. (2020)
<doi:10.1038/s41597-020-0453-3>). Computes heat stress indices, including
wet-bulb globe temperature (Liljegren et al. (2008)
<doi:10.1080/15459620802310770>) and the Universal Thermal Climate Index
(Bröde et al. (2012) <doi:10.1007/s00484-011-0454-1>), and heatwave
indicators, including the Excess Heat Factor (Nairn and Fawcett (2015)
<doi:10.3390/ijerph120100227>).

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
