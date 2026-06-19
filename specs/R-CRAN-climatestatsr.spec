%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  climatestatsr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Climate Change Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
A comprehensive collection of statistical functions for climate change
research. Provides tools for temporal trend detection based on the
Mann-Kendall (MK) test (Mann 1945 <doi:10.2307/1907187>; Kendall 1975,
ISBN:0852641990) and Sen's slope (Sen 1968 <doi:10.2307/2285891>), spatial
autocorrelation using Moran's I (Moran 1950 <doi:10.2307/2332142>),
extreme value analysis using the Generalised Extreme Value (GEV)
distribution and Peaks-Over-Threshold (POT) method (Coles 2001
<doi:10.1007/978-1-4471-3675-0>), standardised drought indices including
the Standardised Precipitation Index (SPI; McKee et al. 1993) and the
Standardised Precipitation Evapotranspiration Index (SPEI; Vicente-Serrano
et al. 2010 <doi:10.1175/2009JCLI2909.1>), and formal
detection-attribution methods via optimal fingerprint regression and
Empirical Orthogonal Function (EOF) analysis (Allen and Tett 1999
<doi:10.1007/s003820050291>), and apparent temperature via the heat index
(Steadman 1979 <doi:10.1175/1520-0450(1979)018%%3C0861:TAOSPI%%3E2.0.CO;2>).
Suitable for both station-level time series and gridded climate fields.

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
