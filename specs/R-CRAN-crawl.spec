%global packname  crawl
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          3%{?dist}
Summary:          Fit Continuous-Time Correlated Random Walk Models to AnimalMovement Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-rmapshaper 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-mvtnorm 
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-rmapshaper 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 

%description
Fit continuous-time correlated random walk models with time indexed
covariates to animal telemetry data. The model is fit using the
Kalman-filter on a state space version of the continuous-time stochastic
movement process.

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
%{rlibdir}/%{packname}/libs
