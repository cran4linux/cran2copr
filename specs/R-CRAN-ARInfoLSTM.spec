%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ARInfoLSTM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          ARIMA-Informed LSTM for Time Series Forecasting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.21
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-torch >= 0.11.0
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-forecast >= 8.21
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-torch >= 0.11.0
Requires:         R-CRAN-coro 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements an ARIMA-Informed Long Short-Term Memory (LSTM) framework for
univariate time series forecasting. The package integrates statistical
information extracted from AutoRegressive Integrated Moving Average
(ARIMA) models with deep learning-based LSTM architectures to improve
forecasting accuracy, stability, and interpretability. Inspired by the
philosophy of Physics-Informed Machine Learning (PIML), the proposed
framework incorporates information from classical statistical models into
neural network learning, creating a hybrid forecasting approach that
combines domain knowledge with data-driven intelligence. The methodology
is motivated by hybrid forecasting framework proposed by Yeasin and Paul
(2024) <doi:10.1007/s11227-023-05542-3>.

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
