%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  imputeCGM
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Impute Missing Glucose Values in CGM Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-CGManalyzer 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-CGManalyzer 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-shiny 

%description
Imputes missing glucose values in repeated-measures continuous glucose
monitoring (CGM) data. Workflows create time-series features from raw
timestamps, support model selection, and return the user's original
columns plus an imputed glucose column. Methods include multiple
imputation by chained equations using 'mice' (Azur et al. (2011)
<doi:10.1002/mpr.329>), Random Forest regression using 'ranger' (Breiman
(2001) <doi:10.1023/A:1010933404324>), k-nearest-neighbor regression using
'FNN' (Zhang (2016) <doi:10.21037/atm.2016.03.37>), 'XGBoost' using
'xgboost' (Chen and Guestrin (2016) <doi:10.1145/2939672.2939785>),
'LightGBM' using 'lightgbm' (Ke et al. (2017)
<https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision>),
and ARIMA forecasting using 'forecast' (Hyndman and Khandakar (2008)
<doi:10.18637/jss.v027.i03>). A 'Python'-compatible backend uses
'reticulate' to call 'pandas', 'scikit-learn', 'statsmodels', 'xgboost',
and optional 'lightgbm'.

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
