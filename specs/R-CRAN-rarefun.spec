%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rarefun
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Rare Events Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-isotree 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pdp 
BuildRequires:    R-stats 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-isotree 
Requires:         R-CRAN-Rdpack 
Requires:         R-parallel 
Requires:         R-CRAN-pdp 
Requires:         R-stats 

%description
Functions for detecting and analyzing rare events in data. Implements
isolation forest (Liu et al., 2008, <doi:10.1109/ICDM.2008.17>) and
clustering for anomaly detection in time series residuals. Decomposes time
series using LOESS (Locally Estimated Scatterplot Smoothing) or STL
(Seasonal-Trend decomposition using LOESS). Detects marine heatwaves and
cold spells following Hobday et al. (2016)
<doi:10.1016/j.pocean.2015.12.014>. Provides goodness-of-fit tests for
quantile regression (Haupt et al., 2011,
<doi:10.1080/02664763.2011.573542>), partial dependence with quantile
random forests, MCC (Matthews Correlation Coefficient) computation and
testing, knee-point detection via the Kneedle algorithm (Satopaa et al.,
2011, <doi:10.1109/ICDCSW.2011.20>), and spatial point matching.

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
