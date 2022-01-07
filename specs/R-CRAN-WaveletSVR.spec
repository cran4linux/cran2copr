%global __brp_check_rpaths %{nil}
%global packname  WaveletSVR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet-SVR Hybrid Model for Time Series Forecasting

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
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-tsutils 
Requires:         R-stats 
Requires:         R-CRAN-wavelets 
Requires:         R-CRAN-fracdiff 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-tsutils 

%description
The main aim of this package is to combine the advantage of wavelet and
support vector machine models for time series forecasting. This package
also gives the accuracy measurements in terms of RMSE and MAPE. This
package fits the hybrid Wavelet SVR model for time series forecasting The
main aim of this package is to combine the advantage of wavelet and
Support Vector Regression (SVR) models for time series forecasting. This
package also gives the accuracy measurements in terms of Root Mean Square
Error (RMSE) and Mean Absolute Prediction Error (MAPE). This package is
based on the algorithm of Raimundo and Okamoto (2018) <DOI:
10.1109/INFOCT.2018.8356851>.

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
