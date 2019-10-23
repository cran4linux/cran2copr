%global packname  tsensembler
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Dynamic Ensembles for Time Series Forecasting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-opera 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-softImpute 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-RcppRoll 
Requires:         R-methods 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-Cubist 
Requires:         R-nnet 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-opera 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-softImpute 

%description
A framework for dynamically combining forecasting models for time series
forecasting predictive tasks. It leverages machine learning models from
other packages to automatically combine expert advice using metalearning
and other state-of-the-art forecasting combination approaches. The
predictive methods receive a data matrix as input, representing an
embedded time series, and return a predictive ensemble model. The ensemble
use generic functions 'predict()' and 'forecast()' to forecast future
values of the time series. Moreover, an ensemble can be updated using
methods, such as 'update_weights()' or 'update_base_models()'. A complete
description of the methods can be found in: Cerqueira, V., Torgo, L.,
Pinto, F., and Soares, C. "Arbitrated Ensemble for Time Series
Forecasting." to appear at: Joint European Conference on Machine Learning
and Knowledge Discovery in Databases. Springer International Publishing,
2017; and Cerqueira, V., Torgo, L., and Soares, C.: "Arbitrated Ensemble
for Solar Radiation Forecasting." International Work-Conference on
Artificial Neural Networks. Springer, 2017
<doi:10.1007/978-3-319-59153-7_62>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
