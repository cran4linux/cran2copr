%global packname  prophet
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          3%{?dist}
Summary:          Automatic Forecasting Procedure

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-CRAN-BH
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-dygraphs >= 1.1.1.4
BuildRequires:    R-CRAN-dplyr >= 0.7.7
BuildRequires:    R-CRAN-tidyr >= 0.6.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-rlang >= 0.3.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-dygraphs >= 1.1.1.4
Requires:         R-CRAN-dplyr >= 0.7.7
Requires:         R-CRAN-tidyr >= 0.6.1
Requires:         R-CRAN-rlang >= 0.3.0.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-xts 

%description
Implements a procedure for forecasting time series data based on an
additive model where non-linear trends are fit with yearly, weekly, and
daily seasonality, plus holiday effects. It works best with time series
that have strong seasonal effects and several seasons of historical data.
Prophet is robust to missing data and shifts in the trend, and typically
handles outliers well.

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
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/stan
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
