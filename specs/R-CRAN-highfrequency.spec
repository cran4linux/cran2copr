%global packname  highfrequency
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Tools for Highfrequency Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-timeDate 
Requires:         R-MASS 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readr 

%description
Provide functionality to manage, clean and match highfrequency trades and
quotes data, calculate various liquidity measures, estimate and forecast
volatility, detect price jumps and investigate microstructure noise and
intraday periodicity.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
