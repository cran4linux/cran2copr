%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TrendSLR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Trend, Velocity, and Acceleration from Sea Level Records

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Rssa 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-imputeTS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Rssa 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-imputeTS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Provides tools for analysing annual average ocean water level time series,
estimating mean sea level trends, velocities, and accelerations using
Singular Spectrum Analysis (SSA). The detailed methodology for resolving
mean sea level with improved temporal resolution follows Watson (2018)
"Improved Techniques to Estimate Mean Sea Level, Velocity and Acceleration
from Long Ocean Water Level Time Series to Augment Sea Level (and Climate
Change) Research"
<https://unsworks.unsw.edu.au/entities/publication/5e835c87-aa0a-4457-807e-29d354e91d45>.
Additional methodological developments and applications are described in
Watson (2020) "Status of Mean Sea Level Rise around the USA"
<doi:10.3390/geohazards2020005> and Watson and Lim (2020) "An Update on
the Status of Mean Sea Level Rise around the Korean Peninsula"
<doi:10.3390/atmos11111153>. Includes multiple gap-filling methods for
incomplete records, diagnostic tools for inspecting SSA components, and
plotting functions for generating publication-quality screen and file
outputs.

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
