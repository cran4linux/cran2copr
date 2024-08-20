%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sits
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Satellite Image Time Series Analysis for Earth Observation Data Cubes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-parallel >= 4.0.5
BuildRequires:    R-CRAN-tibble >= 3.1
BuildRequires:    R-CRAN-terra >= 1.7.65
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-sf >= 1.0.12
BuildRequires:    R-CRAN-rstac >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-slider >= 0.2.0
BuildRequires:    R-CRAN-torch >= 0.11.0
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-gdalUtilities 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-parallel >= 4.0.5
Requires:         R-CRAN-tibble >= 3.1
Requires:         R-CRAN-terra >= 1.7.65
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-sf >= 1.0.12
Requires:         R-CRAN-rstac >= 1.0.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-slider >= 0.2.0
Requires:         R-CRAN-torch >= 0.11.0
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-gdalUtilities 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-sysfonts 
Requires:         R-stats 
Requires:         R-CRAN-units 
Requires:         R-utils 

%description
An end-to-end toolkit for land use and land cover classification using big
Earth observation data, based on machine learning methods applied to
satellite image data cubes, as described in Simoes et al (2021)
<doi:10.3390/rs13132428>. Builds regular data cubes from collections in
AWS, Microsoft Planetary Computer, Brazil Data Cube, Copernicus Data Space
Environment (CDSE), Digital Earth Africa, Digital Earth Australia, NASA
HLS using the Spatio-temporal Asset Catalog (STAC) protocol
(<https://stacspec.org/>) and the 'gdalcubes' R package developed by Appel
and Pebesma (2019) <doi:10.3390/data4030092>. Supports visualization
methods for images and time series and smoothing filters for dealing with
noisy time series. Includes functions for quality assessment of training
samples using self-organized maps as presented by Santos et al (2021)
<doi:10.1016/j.isprsjprs.2021.04.014>. Provides machine learning methods
including support vector machines, random forests, extreme gradient
boosting, multi-layer perceptrons, temporal convolutional neural networks
proposed by Pelletier et al (2019) <doi:10.3390/rs11050523>, and temporal
attention encoders by Garnot and Landrieu (2020)
<doi:10.48550/arXiv.2007.00586>. Supports GPU processing of deep learning
models using torch <https://torch.mlverse.org/>. Performs efficient
classification of big Earth observation data cubes and includes functions
for post-classification smoothing based on Bayesian inference, and methods
for active learning and uncertainty assessment. Supports object-based time
series analysis using package supercells
<https://jakubnowosad.com/supercells/>. Enables best practices for
estimating area and assessing accuracy of land change as recommended by
Olofsson et al (2014) <doi:10.1016/j.rse.2014.02.015>. Minimum recommended
requirements: 16 GB RAM and 4 CPU dual-core.

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
