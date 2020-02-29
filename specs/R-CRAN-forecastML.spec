%global packname  forecastML
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}
Summary:          Time Series Forecasting with Machine Learning Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-future.apply >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.12.6
BuildRequires:    R-CRAN-dtplyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-future.apply >= 1.3.0
Requires:         R-CRAN-data.table >= 1.12.6
Requires:         R-CRAN-dtplyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-methods 

%description
The purpose of 'forecastML' is to simplify the process of multi-step-ahead
forecasting with standard machine learning algorithms. 'forecastML'
supports lagged, dynamic, static, and grouping features for modeling
single and grouped numeric or factor/sequence time series. In addition,
simple wrapper functions are used to support model-building with most R
packages. This approach to forecasting is inspired by Bergmeir, Hyndman,
and Koo's (2018) paper "A note on the validity of cross-validation for
evaluating autoregressive time series prediction"
<doi:10.1016/j.csda.2017.11.003>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
