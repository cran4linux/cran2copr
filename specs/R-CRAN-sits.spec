%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sits
%global packver   1.5.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Satellite Image Time Series Analysis for Earth Observation Data Cubes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-tmap >= 4.1
BuildRequires:    R-CRAN-tibble >= 3.3.0
BuildRequires:    R-CRAN-yaml >= 2.3.0
BuildRequires:    R-CRAN-leaflet >= 2.2.2
BuildRequires:    R-CRAN-terra >= 1.8.54
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-httr2 >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-sf >= 1.0.19
BuildRequires:    R-CRAN-rstac >= 1.0.1
BuildRequires:    R-CRAN-luz >= 0.4.0
BuildRequires:    R-CRAN-slider >= 0.2.0
BuildRequires:    R-CRAN-torch >= 0.15.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-leafgl 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-tmap >= 4.1
Requires:         R-CRAN-tibble >= 3.3.0
Requires:         R-CRAN-yaml >= 2.3.0
Requires:         R-CRAN-leaflet >= 2.2.2
Requires:         R-CRAN-terra >= 1.8.54
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-httr2 >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-sf >= 1.0.19
Requires:         R-CRAN-rstac >= 1.0.1
Requires:         R-CRAN-luz >= 0.4.0
Requires:         R-CRAN-slider >= 0.2.0
Requires:         R-CRAN-torch >= 0.15.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-leafgl 
Requires:         R-CRAN-lubridate 
Requires:         R-parallel 
Requires:         R-CRAN-randomForest 
Requires:         R-stats 
Requires:         R-CRAN-units 
Requires:         R-utils 

%description
An end-to-end toolkit for land use and land cover classification using big
Earth observation data. Builds satellite image data cubes from cloud
collections. Supports visualization methods for images and time series and
smoothing filters for dealing with noisy time series. Enables merging of
multi-source imagery (SAR, optical, DEM). Includes functions for quality
assessment of training samples using self-organized maps and to reduce
training samples imbalance. Provides machine learning algorithms including
support vector machines, random forests, extreme gradient boosting,
multi-layer perceptrons, temporal convolution neural networks, and
temporal attention encoders. Performs efficient classification of big
Earth observation data cubes and includes functions for
post-classification smoothing based on Bayesian inference. Enables best
practices for estimating area and assessing accuracy of land change.
Includes object-based spatio-temporal segmentation for space-time OBIA.
Minimum recommended requirements: 16 GB RAM and 4 CPU dual-core.

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
