%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ERA5Flux
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Improve the Utility of ERA5-Land Data at AmeriFlux Site Locations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ecmwfr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-lutz 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ecmwfr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-lutz 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-stats 
Requires:         R-CRAN-terra 

%description
Collection of tools useful for workflows involving ERA5-Land and AmeriFlux
data. Includes functions for downloading ERA5-Land data based on AmeriFlux
sites, formatting the downloaded data to match AmeriFlux standards,
merging both datasets together to ensure consistent timestamps, and
blending them to create a single gap-filled time series. For more details,
visit the Climate Data Store's catalogue entry for ERA5-Land at
<https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land> and the
AmeriFlux homepage at <https://ameriflux.lbl.gov>.

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
