%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AllMetrics
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating Multiple Performance Metrics of a Prediction Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides a function to calculate multiple performance metrics for actual
and predicted values. In total eight metrics will be calculated for
particular actual and predicted series. Helps to describe a Statistical
model's performance in predicting a data. Also helps to compare various
models' performance. The metrics are Root Mean Squared Error (RMSE),
Relative Root Mean Squared Error (RRMSE), Mean absolute Error (MAE), Mean
absolute percentage error (MAPE), Mean Absolute Scaled Error (MASE),
Nash-Sutcliffe Efficiency (NSE), Willmott’s Index (WI), and Legates and
McCabe Index (LME). Among them, first five are expected to be lesser
whereas, the last three are greater the better. More details can be found
from Garai and Paul (2023) <doi:10.1016/j.iswa.2023.200202>.

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
