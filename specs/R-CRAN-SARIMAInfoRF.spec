%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SARIMAInfoRF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          SARIMA-Informed Random Forest for Time Series Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cli 
Requires:         R-stats 
Requires:         R-utils 

%description
Trains a Random Forest on a target blended with the forecasts of a
seasonal autoregressive integrated moving average (SARIMA) model, which
acts as a teacher. For squared error, the composite loss (1 - lambda) *
MSE(f, y) + lambda * MSE(f, y_SARIMA), where MSE is the mean squared
error, is minimised exactly by fitting the forest to the blended target z
= (1 - lambda) * y + lambda * y_SARIMA. The SARIMA model is chosen
automatically by the Akaike information criterion (AIC) or specified
manually; the forest hyperparameters are set manually, by grid search, or
by Bayesian optimisation. The best lambda is chosen on a chronological
validation period. Functions for out-of-sample forecasting, accuracy
measures and plots are provided. The methodology is motivated by hybrid
forecasting framework proposed by Yeasin and Paul (2024)
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
