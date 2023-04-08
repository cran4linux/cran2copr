%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CEEMDANML
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          CEEMDAN Decomposition Based Hybrid Machine Learning Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rlibeemd 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-aTSA 
BuildRequires:    R-CRAN-FinTS 
BuildRequires:    R-CRAN-LSTS 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-pso 
Requires:         R-stats 
Requires:         R-CRAN-Rlibeemd 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-aTSA 
Requires:         R-CRAN-FinTS 
Requires:         R-CRAN-LSTS 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-pso 

%description
Noise in the time-series data significantly affects the accuracy of the
Machine Learning (ML) models (Artificial Neural Network and Support Vector
Regression are considered here). Complete Ensemble Empirical Mode
Decomposition with Adaptive Noise (CEEMDAN) decomposes the time series
data into sub-series and help to improve the model performance. The models
can achieve higher prediction accuracy than the traditional ML models. Two
models have been provided here for time series forecasting. More
information may be obtained from Garai and Paul (2023)
<doi:10.1016/j.iswa.2023.200202>.

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
