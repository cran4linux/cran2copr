%global packname  forecast
%global packver   8.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.12
Release:          2%{?dist}
Summary:          Forecasting Functions for Time Series and Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.35
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-fracdiff 
Requires:         R-graphics 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-magrittr 
Requires:         R-nnet 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-zoo 

%description
Methods and tools for displaying and analysing univariate time series
forecasts including exponential smoothing via state space models and
automatic ARIMA modelling.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
