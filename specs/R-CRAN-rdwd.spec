%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdwd
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Select and Download Climate Data from 'DWD' (German Weather Service)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-berryFunctions >= 1.21.11
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-berryFunctions >= 1.21.11
Requires:         R-CRAN-pbapply 

%description
Handle climate data from the 'DWD' ('Deutscher Wetterdienst', see
<https://www.dwd.de/EN/climate_environment/cdc/cdc_node_en.html> for more
information). Choose observational time series from meteorological
stations with 'selectDWD()'. Find raster data from radar and interpolation
according to <https://bookdown.org/brry/rdwd/raster-data.html>. Download
(multiple) data sets with progress bars and no re-downloads through
'dataDWD()'. Read both tabular observational data and binary gridded
datasets with 'readDWD()'.

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
