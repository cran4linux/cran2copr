%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clim4health
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Post-Processing of Climate Data for Health Applications

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CSTools 
BuildRequires:    R-CRAN-ecmwfr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GHRexplore 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-s2dv 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-CSDownscale 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-ggpattern 
BuildRequires:    R-CRAN-startR 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-CSTools 
Requires:         R-CRAN-ecmwfr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GHRexplore 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-s2dv 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-units 
Requires:         R-CRAN-CSDownscale 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-ggpattern 
Requires:         R-CRAN-startR 
Requires:         R-CRAN-rlang 

%description
Obtain, transform and export climate data including reanalyses, (seasonal)
forecasts and hindcasts, and weather stations for their use in
epidemiological analyses. It is organised in three sequential blocks,
input (download and load data), transform (downscaling, verification,
spatiotemporal aggregation and threshold-based indicators) and output
(visualising and exporting data). Downscaling methods include those
described in Duzenli et al. (2026) <doi:10.1038/s41598-026-45067-2> and
verification methods are based on those in Manubens et al. (2018)
<doi:10.1016/j.envsoft.2018.01.018>.

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
