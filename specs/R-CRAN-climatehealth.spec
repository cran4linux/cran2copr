%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  climatehealth
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tools for Modelling Climate-Health Impacts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tsModel >= 0.6.2
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dlnm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Epi 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-gnm 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-mixmeta 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-tsModel >= 0.6.2
Requires:         R-CRAN-car 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dlnm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Epi 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-gnm 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-mixmeta 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-CRAN-tseries 
Requires:         R-utils 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-zoo 

%description
Tools for producing climate-health indicators and supporting official
statistics from health and climate data. Implements analytical workflows
for temperature-related mortality, wildfire smoke exposure, air pollution,
suicides related to extreme heat, malaria, and diarrhoeal disease
outcomes, with utilities for descriptive statistics, model validation,
attributable fraction and attributable number estimation, relative risk
estimation, minimum mortality temperature estimation, and plotting for
reporting. These six indicators are endorsed by the United Nations
Statistical Commission for inclusion in the Global Set of Environment and
Climate Change Statistics. Implemented methods include distributed lag
non-linear models (DLNM), quasi-Poisson time-series regression,
case-crossover analysis, Bayesian spatio-temporal models using the
Integrated Nested Laplace Approximation ('INLA'), and multivariate
meta-analysis for sub-national estimates. The package is based on methods
developed in the Standards for Official Statistics on Climate-Health
Interactions (SOSCHI) project
<https://climate-health.officialstatistics.org>. For methodologies, see
Watkins et al. (2025) <doi:10.5281/zenodo.14865904>, Brown et al. (2024)
<doi:10.5281/zenodo.14052183>, Pearce et al. (2024)
<doi:10.5281/zenodo.14050224>, Byukusenge et al. (2025)
<doi:10.5281/zenodo.15585042>, Dzakpa et al. (2025)
<doi:10.5281/zenodo.14881886>, and Dzakpa et al. (2025)
<doi:10.5281/zenodo.14871506>.

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
