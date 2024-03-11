%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hockeystick
%global packver   0.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.4
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Visualize Essential Climate Change Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-treemapify 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-tools 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-treemapify 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-jsonlite 

%description
Provides easy access to essential climate change datasets to non-climate
experts. Users can download the latest raw data from authoritative sources
and view it via pre-defined 'ggplot2' charts. Datasets include atmospheric
CO2, methane, emissions, instrumental and proxy temperature records, sea
levels, Arctic/Antarctic sea-ice, Hurricanes, and Paleoclimate data.
Sources include: NOAA Mauna Loa Laboratory
<https://gml.noaa.gov/ccgg/trends/data.html>, Global Carbon Project
<https://www.globalcarbonproject.org/carbonbudget/>, NASA GISTEMP
<https://data.giss.nasa.gov/gistemp/>, National Snow and Sea Ice Data
Center <https://nsidc.org/home>, CSIRO
<https://research.csiro.au/slrwavescoast/sea-level/measurements-and-data/sea-level-data/>,
NOAA Laboratory for Satellite Altimetry
<https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/> and HURDAT
Atlantic Hurricane Database
<https://www.aoml.noaa.gov/hrd/hurdat/Data_Storm.html>, Vostok Paleo
carbon dioxide and temperature data: <doi:10.3334/CDIAC/ATG.009>.

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
