%global packname  forecastHybrid
%global packver   4.2.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.17
Release:          1%{?dist}
Summary:          Convenient Functions for Ensemble Time Series Forecasts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-zoo >= 1.7
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-thief 
Requires:         R-CRAN-forecast >= 8.1
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-zoo >= 1.7
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-thief 

%description
Convenient functions for ensemble forecasts in R combining approaches from
the 'forecast' package. Forecasts generated from auto.arima(), ets(),
thetaf(), nnetar(), stlm(), tbats(), and snaive() can be combined with
equal weights, weights based on in-sample errors (introduced by Bates &
Granger (1969) <doi:10.1057/jors.1969.103>), or cross-validated weights.
Cross validation for time series data with user-supplied models and
forecasting functions is also supported to evaluate model accuracy.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/davidshaub@gmx.com.key
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
