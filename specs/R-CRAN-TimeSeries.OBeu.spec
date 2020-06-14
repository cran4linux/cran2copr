%global packname  TimeSeries.OBeu
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          2%{?dist}
Summary:          Time Series Analysis 'OpenBudgets.eu'

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-trend 
BuildRequires:    R-CRAN-tseries 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-trend 
Requires:         R-CRAN-tseries 

%description
Estimate and return the needed parameters for visualizations designed for
'OpenBudgets.eu' <http://openbudgets.eu/> time series data. Calculate time
series model and forecast parameters in budget time series data of
municipalities across Europe, according to the 'OpenBudgets.eu' data
model. There are functions for measuring deterministic and stochastic
trend of the input time series data with 'ACF', 'PACF', 'Phillips Perron'
test, 'Augmented Dickey Fuller (ADF)' test,
'Kwiatkowski-Phillips-Schmidt-Shin (KPSS)' test, 'Mann Kendall' test for
monotonic trend and 'Cox and Stuart' trend test, decomposing with local
regression models or 'stl' decomposition, fitting the appropriate 'arima'
model and provide forecasts for the input 'OpenBudgets.eu' time series
fiscal data. Also, can be used generally to extract visualization
parameters convert them to 'JSON' format and use them as input in a
different graphical interface.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
