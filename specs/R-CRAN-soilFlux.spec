%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  soilFlux
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Physics-Informed Neural Networks for Soil Water Retention Curves

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.2.0
BuildRequires:    R-CRAN-tensorflow >= 2.14.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-reticulate >= 1.34.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-tensorflow >= 2.14.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-reticulate >= 1.34.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0

%description
Implements a physics-informed one-dimensional convolutional neural network
(CNN1D-PINN) for estimating the complete soil water retention curve (SWRC)
as a continuous function of matric potential, from soil texture, organic
carbon, bulk density, and depth. The network architecture ensures strict
monotonic decrease of volumetric water content with increasing suction by
construction, through cumulative integration of non-negative slope outputs
(monotone integral architecture). Four physics-based residual constraints
adapted from Norouzi et al. (2025) <doi:10.1029/2024WR038149> are embedded
in the loss function: (S1) linearity at the dry end (pF in [5, 7.6]); (S2)
non-negativity at pF = 6.2; (S3) non-positivity at pF = 7.6; and (S4) a
near-zero derivative in the saturated plateau region (pF in [-2, -0.3]).
Includes tools for data preparation, model training, dense prediction,
performance metrics, texture classification, and publication-quality
visualisation.

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
