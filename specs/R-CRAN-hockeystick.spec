%global packname  hockeystick
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Visualize Essential Climate Change Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-viridisLite 

%description
Provides easy access to essential climate change datasets to non-climate
experts. Users can download the latest raw data from authoritative sources
and view it via pre-defined 'ggplot2' charts. Datasets include atmospheric
CO2, instrumental and proxy temperature records, sea levels,
Arctic/Antarctic sea-ice, and Paleoclimate data. Sources include: NOAA
Mauna Loa Laboratory
<https://www.esrl.noaa.gov/gmd/ccgg/trends/data.html>, NASA GISTEMP
<https://data.giss.nasa.gov/gistemp/>, National Snow and Sea Ice Data
Center <https://nsidc.org/data/seaice_index/archives>, CSIRO
<http://www.cmar.csiro.au/sealevel/sl_data_cmar.html>, NOAA Laboratory for
Satellite Altimetry
<https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/>, Vostok Paleo
carbon dioxide and temperature data:
<https://cdiac.ess-dive.lbl.gov/trends/co2/vostok.html>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
