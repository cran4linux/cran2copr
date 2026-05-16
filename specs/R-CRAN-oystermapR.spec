%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oystermapR
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predict and Map Oyster Growth Suitability from Environmental Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-terra >= 1.7.18
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-terra >= 1.7.18
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-stats 
Requires:         R-utils 

%description
Predicts spatial suitability for oyster growth from environmental survey
data using Analytic Hierarchy Process (AHP) weighted scoring. Users supply
sensor data from Acoustic Doppler Current Profilers (ADCP),
Conductivity-Temperature-Depth (CTD) sensors, bathymetric sonar, and
sidescan sonar, specify a target species, and receive per-location
suitability scores, a 'GeoTIFF' heatmap for 'QGIS', contour lines, and a
formatted PDF or HTML report. Supports fourteen species across global
aquaculture regions, including Ostrea edulis, Magallana gigas, Crassostrea
virginica, Crassostrea hongkongensis, and ten further species; see
list_species(). Includes season-aware scoring, tidal height correction,
Bayesian tolerance parameter updating from field observations, spatial
block cross-validation (Roberts et al., 2017, <doi:10.1111/ecog.02881>),
permutation variable importance, wave exposure and sediment stability
modules, Harmful Algal Bloom (HAB) risk and anthropogenic disturbance
scoring with optional live International Council for the Exploration of
the Sea (ICES) data integration, hybrid larval dispersal connectivity
scoring (union-find Gaussian kernel plus optional 'OpenDrift' or Finite
Volume Community Ocean Model ('FVCOM') connectivity matrix), and batch
multi-species comparison.

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
