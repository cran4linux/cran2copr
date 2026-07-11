%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CDSimX
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Climate Data for Research and Modelling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
Advanced climate simulation, forecasting, visualization, export, and
machine learning tools. Generates synthetic climate datasets for single or
multiple weather stations using stochastic weather generation techniques.
'CDSimX' simulates daily climate variables including minimum and maximum
temperature, rainfall, relative humidity, solar radiation, wind speed,
wind direction, dew point temperature, and potential evapotranspiration.
The package incorporates seasonal harmonic models, Markov chain rainfall
occurrence processes, Gamma-distributed rainfall amounts, copula-based
dependence structures, bias-correction procedures, and physical
consistency constraints. 'CDSimX' supports climate data generation,
environmental modeling, machine learning benchmarking, sensitivity
analysis, and educational applications. Methods are based on established
stochastic weather generation approaches described in Richardson (1981)
<doi:10.1029/WR017i001p00182>, Wilks (1999)
<doi:10.1016/S0168-1923(99)00037-4>, and Osei et al. (2026)
<doi:10.5334/jors.666>.

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
