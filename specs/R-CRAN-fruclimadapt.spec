%global __brp_check_rpaths %{nil}
%global packname  fruclimadapt
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluation Tools for Assessing Climate Adaptation of Fruit Tree Species

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-lubridate 

%description
Climate is a critical component limiting growing range of plant species,
which also determines cultivar adaptation to a region. The evaluation of
climate influence on fruit production is critical for decision-making in
the design stage of orchards and vineyards and in the evaluation of the
potential consequences of future climate. Bio- climatic indices and plant
phenology are commonly used to describe the suitability of climate for
growing quality fruit and to provide temporal and spatial information
about regarding ongoing and future changes. 'fruclimadapt' streamlines the
assessment of climate adaptation and the identification of potential risks
for grapevines and fruit trees. Procedures in the package allow to i)
downscale daily meteorological variables to hourly values (Forster et al
(2016) <doi:10.5194/gmd-9-2315-2016>), ii) estimate chilling and forcing
heat accumulation (Miranda et al (2019)
<https://ec.europa.eu/eip/agriculture/sites/agri-eip/files/fg30_mp5_phenology_critical_temperatures.pdf>),
iii) estimate plant phenology (Schwartz (2012)
<doi:10.1007/978-94-007-6925-0>), iv) calculate bioclimatic indices to
evaluate fruit tree and grapevine adaptation (e.g. Badr et al (2017)
<doi:10.3354/cr01532>), v) estimate the incidence of weather-related
disorders in fruits (e.g. Snyder and de Melo-Abreu (2005,
ISBN:92-5-105328-6) and vi) estimate plant water requirements (Allen et al
(1998, ISBN:92-5-104219-5)).

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
