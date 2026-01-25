%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  growthTrendR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Toolkit for Data Processing, Quality, and Statistical Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 7.0.0
BuildRequires:    R-stats >= 4.3.2
BuildRequires:    R-CRAN-raster >= 3.6.26
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-nlme >= 3.0.0
BuildRequires:    R-CRAN-mgcv >= 1.8.0
BuildRequires:    R-CRAN-terra >= 1.7.71
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-future >= 1.34.0
BuildRequires:    R-CRAN-data.table >= 1.17.8
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-patchwork >= 1.0.0
BuildRequires:    R-CRAN-htmltools >= 0.5.9
BuildRequires:    R-CRAN-furrr >= 0.3.1
BuildRequires:    R-CRAN-pryr >= 0.1.6
Requires:         R-CRAN-curl >= 7.0.0
Requires:         R-stats >= 4.3.2
Requires:         R-CRAN-raster >= 3.6.26
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-nlme >= 3.0.0
Requires:         R-CRAN-mgcv >= 1.8.0
Requires:         R-CRAN-terra >= 1.7.71
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-future >= 1.34.0
Requires:         R-CRAN-data.table >= 1.17.8
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-patchwork >= 1.0.0
Requires:         R-CRAN-htmltools >= 0.5.9
Requires:         R-CRAN-furrr >= 0.3.1
Requires:         R-CRAN-pryr >= 0.1.6

%description
Offers tools for data formatting, anomaly detection, and classification of
tree-ring data using spatial comparisons and cross-correlation. Supports
flexible detrending and climate–growth modeling via generalized additive
mixed models (Wood 2017, ISBN:978-1498728331) and the 'mgcv' package
(<https://CRAN.R-project.org/package=mgcv>), enabling robust analysis of
non-linear trends and autocorrelated data. Provides standardized visual
reporting, including summaries, diagnostics, and model performance.
Compatible with '.rwl' files and tailored for the Canadian Forest Service
Tree-Ring Data (CFS-TRenD) repository (Girardin et al. (2021)
<doi:10.1139/er-2020-0099>), offering a comprehensive and adaptable
framework for dendrochronologists working with large and complex datasets.

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
