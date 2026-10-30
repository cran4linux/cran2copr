%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RWInfoLSTM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random Walk-Informed LSTM for Time Series Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-torch >= 0.11.0
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-torch >= 0.11.0
Requires:         R-CRAN-coro 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements a Random Walk (RW)-informed Long Short-Term Memory (LSTM)
network for univariate time series forecasting. The LSTM is trained on the
full series with a composite loss that blends the usual mean squared error
(MSE) between predictions and observations with the MSE between
predictions and the fitted Random Walk, weighted by a parameter lambda (0
gives a standard LSTM, 1 gives a fully RW-guided LSTM). The Random Walk,
either simple or with drift, is selected automatically by its in-sample
root mean squared error (RMSE), and the lambda value with the lowest
training RMSE is retained. The LSTM hyperparameters can be supplied
manually or tuned by grid search, and functions for out-of-sample
forecasting, accuracy measures and plots are provided. The methodology is
motivated by hybrid forecasting framework proposed by Yeasin and Paul
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
