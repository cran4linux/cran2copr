%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OptiSembleForecasting
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimization Based Ensemble Forecasting Using MCS Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-tsutils 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-MCS 
BuildRequires:    R-CRAN-caretForecast 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-CRAN-metaheuristicOpt 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-tsutils 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-MCS 
Requires:         R-CRAN-caretForecast 
Requires:         R-CRAN-kknn 
Requires:         R-CRAN-metaheuristicOpt 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-factoextra 
Requires:         R-utils 

%description
The real-life data is complex in nature. No single model can capture all
aspect of complex time series data. In this package, 14 models, namely
Recurrent Neural Network (RNN), Gated Recurrent Unit (GRU), Long
Short-Term Memory (LSTM), Bidirectional LSTM, Deep LSTM, Artificial Neural
Network (ANN), Support Vector Regression (SVR), Random Forest (RF),
k-Nearest Neighbour (KNN), XGBoost (XGB), Autoregressive Integrated Moving
Average (ARIMA), Error-Trend-Seasonality (ETS) and TBATS models, have been
implemented and their accuracy have been checked. An PCA based error index
has been proposed to select a group of best models using MCS algorithms.
After selecting the models, the forecasts from these models have been
ensembled using optimization techniques. This package allows to implement
20 optimization techniques, namely, Artificial Bee Colony (ABC), Ant Lion
Optimizer (ALO), Bat Algorithm (BA), Black Hole Optimization Algorithm
(BHO), Clonal Selection Algorithm (CLONALG), Cuckoo Search (CS), Cat Swarm
Optimization (CSO), Dragonfly Algorithm (DA), Differential Evolution (DE),
Firefly Algorithm (FFA), Genetic Algorithm (GA), Gravitational Based
Search Algorithm (GBS), Grasshopper Optimisation Algorithm (GOA), Grey
Wolf Optimizer (GWO), Harmony Search Algorithm (HS), Krill-Herd Algorithm
(KH), Moth Flame Optimizer (MFO), Particle Swarm Optimization (PSO), Sine
Cosine Algorithm (SCA), Shuffled Frog Leaping (SFL) and Whale Optimization
Algorithm (WOA). This package has been developed using concept of Wang et
al. (2022) <doi:10.1016/j.apm.2022.09.004>, Qu et al. (2022)
<doi:10.1016/j.eswa.2022.118746> and Kriz (2019)
<doi:10.1007/978-3-030-18195-6_21 >.

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
