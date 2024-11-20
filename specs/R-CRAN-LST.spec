%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LST
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Land Surface Temperature Retrieval for Landsat 8

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-terra 

%description
Calculates Land Surface Temperature from Landsat band 10 and 11. Revision
of the Single-Channel Algorithm for Land Surface Temperature Retrieval
From Landsat Thermal-Infrared Data. Jimenez-Munoz JC, Cristobal J, Sobrino
JA, et al (2009). <doi: 10.1109/TGRS.2008.2007125>. Land surface
temperature retrieval from LANDSAT TM 5. Sobrino JA, Jiménez-Muñoz JC,
Paolini L (2004). <doi:10.1016/j.rse.2004.02.003>. Surface temperature
estimation in Singhbhum Shear Zone of India using Landsat-7 ETM+ thermal
infrared data. Srivastava PK, Majumdar TJ, Bhattacharya AK (2009). <doi:
10.1016/j.asr.2009.01.023>. Mapping land surface emissivity from NDVI:
Application to European, African, and South American areas. Valor E
(1996). <doi:10.1016/0034-4257(96)00039-9>. On the relationship between
thermal emissivity and the normalized difference vegetation index for
natural surfaces. Van de Griend AA, Owe M (1993).
<doi:10.1080/01431169308904400>. Land Surface Temperature Retrieval from
Landsat 8 TIRS—Comparison between Radiative Transfer Equation-Based
Method, Split Window Algorithm and Single Channel Method. Yu X, Guo X, Wu
Z (2014). <doi:10.3390/rs6109829>. Calibration and Validation of land
surface temperature for Landsat8-TIRS sensor. Land product validation and
evolution. Skoković D, Sobrino JA, Jimenez-Munoz JC, Soria G, Julien Y,
Mattar C, Cristóbal J. (2014).

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
