%global packname  modeltime
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          2%{?dist}
Summary:          The Tidymodels Extension for Time Series Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-timetk >= 2.1.0
BuildRequires:    R-CRAN-parsnip >= 0.1.2
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-workflows 
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
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-prophet 
BuildRequires:    R-methods 
Requires:         R-CRAN-timetk >= 2.1.0
Requires:         R-CRAN-parsnip >= 0.1.2
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-dials 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-workflows 
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
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-prophet 
Requires:         R-methods 

%description
The time series forecasting framework for use with the 'tidymodels'
ecosystem. Models include ARIMA, Exponential Smoothing, and additional
time series models from the 'forecast' and 'prophet' packages. Refer to
"Forecasting Principles & Practice, Second edition"
(<https://otexts.com/fpp2/>). Refer to "Prophet: forecasting at scale"
(<https://research.fb.com/blog/2017/02/prophet-forecasting-at-scale/>.).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
