%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  climatekit
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Climate Indices for Temperature, Precipitation, and Drought

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-stats 
BuildRequires:    R-tools 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-stats 
Requires:         R-tools 

%description
Compute the standard suite of climate indices from daily weather
observations. Provides the canonical 'ETCCDI' 27 (Expert Team on Climate
Change Detection and Indices), the 'ET-SCI' heatwave and cold-wave
families plus the Excess Heat Factor of Nairn and Fawcett (2013), and
agroclimatic, drought, and human-comfort families. Drought indices ('SPI',
'SPEI') accept a choice of distribution (gamma or Pearson III for SPI;
log-logistic or generalised extreme value for SPEI). Reference
evapotranspiration is available via Hargreaves and the FAO-56
Penman-Monteith method (Allen et al. 1998). Percentile-based indices
support the Zhang (2005) in-base bootstrap. Daily inputs are numeric
vectors plus a 'Date' vector; outputs are tidy data frames. Optional
gridded support via 'terra' applies any index over a 'SpatRaster' and
reads 'netCDF' input. No external API calls; pairs with data packages such
as 'readnoaa'. References: Alexander et al. (2006)
<doi:10.1029/2005JD006290>; Zhang et al. (2011) <doi:10.1002/wcc.147>;
Zhang et al. (2005) <doi:10.1175/JCLI3366.1>.

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
