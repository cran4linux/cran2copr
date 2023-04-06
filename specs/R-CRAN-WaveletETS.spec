%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WaveletETS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet Based Error Trend Seasonality Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wavelets 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-caretForecast 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-tseries 
Requires:         R-stats 
Requires:         R-CRAN-wavelets 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-caretForecast 

%description
ETS stands for Error, Trend, and Seasonality, and it is a popular time
series forecasting method. Wavelet decomposition can be used for
denoising, compression, and feature extraction of signals. By removing the
high-frequency components, wavelet decomposition can remove noise from the
data while preserving important features. A hybrid Wavelet ETS (Error
Trend-Seasonality) model has been developed for time series forecasting
using algorithm of Anjoy and Paul (2017) <DOI:10.1007/s00521-017-3289-9>.

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
