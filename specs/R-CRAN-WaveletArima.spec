%global __brp_check_rpaths %{nil}
%global packname  WaveletArima
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet-ARIMA Model for Time Series Forecasting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wavelets 
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-CRAN-forecast 
Requires:         R-stats 
Requires:         R-CRAN-wavelets 
Requires:         R-CRAN-fracdiff 
Requires:         R-CRAN-forecast 

%description
Noise in the time-series data significantly affects the accuracy of the
ARIMA model. Wavelet transformation decomposes the time series data into
subcomponents to reduce the noise and help to improve the model
performance. The wavelet-ARIMA model can achieve higher prediction
accuracy than the traditional ARIMA model. This package provides
Wavelet-ARIMA model for time series forecasting based on the algorithm by
Aminghafari and Poggi (2012) and Paul and Anjoy (2018)
<doi:10.1142/S0219691307002002> <doi:10.1007/s00704-017-2271-x>.

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
