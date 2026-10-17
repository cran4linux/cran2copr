%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClimateAnomaly
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rainfall and Temperature Anomaly Indices for Climate Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-e1071 
Requires:         R-stats 
Requires:         R-CRAN-e1071 

%description
Computes rainfall anomaly indices and a standardised temperature anomaly
from monthly or annual precipitation and temperature data supplied by the
user. The rainfall indices are the Rainfall Anomaly Index (RAI; Van Rooy,
1965), the Modified Rainfall Anomaly Index (MRAI) and the Standardized
Rainfall Anomaly Index (SRAI) of Ekpetere (2025)
<doi:10.1016/j.jenvman.2025.124160>, the Simplified Standardized
Precipitation Index (SSPI) of Raziei (2021)
<doi:10.1016/j.jhydrol.2021.126761>, and the Standardized Precipitation
Index (SPI; McKee et al., 1993). The temperature anomaly is a z-score
computed within each calendar month. All indices are computed group-wise,
so the user can stratify by any combination of spatial units (state,
district, grid cell) and calendar month, and each value can be classified
into a descriptive severity class.

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
