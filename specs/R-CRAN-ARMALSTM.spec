%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ARMALSTM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting of Hybrid ARMA-LSTM Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-reticulate 

%description
The real-life time series data are hardly pure linear or nonlinear.
Merging a linear time series model like the autoregressive moving average
(ARMA) model with a nonlinear neural network model such as the Long
Short-Term Memory (LSTM) model can be used as a hybrid model for more
accurate modeling purposes. Both the autoregressive integrated moving
average (ARIMA) and autoregressive fractionally integrated moving average
(ARFIMA) models can be implemented. Details can be found in Box et al.
(2015, ISBN: 978-1-118-67502-1) and Hochreiter and Schmidhuber (1997)
<doi:10.1162/neco.1997.9.8.1735>.

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
