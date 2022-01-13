%global __brp_check_rpaths %{nil}
%global packname  modeltime
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Tidymodels Extension for Time Series Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-timetk >= 2.6.0
BuildRequires:    R-CRAN-xgboost >= 1.2.0.1
BuildRequires:    R-CRAN-parsnip >= 0.1.6
BuildRequires:    R-CRAN-workflows >= 0.1.3
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-yardstick >= 0.0.8
BuildRequires:    R-CRAN-StanHeaders 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-prophet 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-timetk >= 2.6.0
Requires:         R-CRAN-xgboost >= 1.2.0.1
Requires:         R-CRAN-parsnip >= 0.1.6
Requires:         R-CRAN-workflows >= 0.1.3
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-yardstick >= 0.0.8
Requires:         R-CRAN-StanHeaders 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-janitor 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-prophet 
Requires:         R-methods 
Requires:         R-CRAN-cli 

%description
The time series forecasting framework for use with the 'tidymodels'
ecosystem. Models include ARIMA, Exponential Smoothing, and additional
time series models from the 'forecast' and 'prophet' packages. Refer to
"Forecasting Principles & Practice, Second edition"
(<https://otexts.com/fpp2/>). Refer to "Prophet: forecasting at scale"
(<https://research.facebook.com/blog/2017/02/prophet-forecasting-at-scale/>.).

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
