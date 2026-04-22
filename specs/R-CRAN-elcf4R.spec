%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  elcf4R
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Electricity Load Curves Forecasting at Individual Level

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-keras3 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-wavelets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-keras3 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-wavelets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 

%description
Implements forecasting methods for individual electricity load curves,
including Kernel Wavelet Functional (KWF), clustered KWF, Generalized
Additive Models (GAM), Multivariate Adaptive Regression Splines (MARS),
and Long Short-Term Memory (LSTM) models. Provides normalized dataset
adapters for iFlex, StoreNet, Low Carbon London, and REFIT; download and
read support for IDEAL and GX; explicit Python backend selection for
TensorFlow-based LSTM fits; helpers for daily segmentation and
rolling-origin benchmarking; and compact shipped example panels and
benchmark-result datasets.

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
