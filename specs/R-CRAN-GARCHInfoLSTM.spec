%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GARCHInfoLSTM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          GARCH-Informed LSTM Model for Volatility Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rugarch >= 1.5.0
BuildRequires:    R-CRAN-torch >= 0.11.0
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rugarch >= 1.5.0
Requires:         R-CRAN-torch >= 0.11.0
Requires:         R-CRAN-coro 
Requires:         R-stats 
Requires:         R-utils 

%description
The proposed Generalized Autoregressive Conditional Heteroskedasticity
(GARCH)-informed Long Short-Term Memory (LSTM) model follows the concept
of physics-informed machine learning (PIML) by integrating established
econometric knowledge of price volatility into a data-driven forecasting
framework. In the model, conditional volatility estimated from the GARCH
process is incorporated as an additional explanatory signal or
volatility-based weighting component within the LSTM architecture. This
enables the LSTM to learn nonlinear temporal dependencies while remaining
informed by the underlying characteristics of agricultural price series,
including volatility clustering, heteroscedasticity and market
uncertainty. The optimized weighting parameter, lambda, controls the
contribution of the GARCH-derived volatility information to the final
prediction. Thus, the model combines the statistical interpretability of
GARCH with the nonlinear learning capability of LSTM, producing a hybrid
PIML framework that is more responsive to both normal price movements and
periods of extreme market volatility. The methodology is motivated by
hybrid forecasting framework proposed by Yeasin and Paul (2024)
<doi:10.1007/s11227-023-05542-3>.

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
