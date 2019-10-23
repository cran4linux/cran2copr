%global packname  rstap
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Spatial Temporal Aggregated Predictor Models via 'stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-nlme >= 3.1.124
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-pracma >= 2.1.4
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0.1
BuildRequires:    R-CRAN-bayesplot >= 1.5.0
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-rstantools >= 1.4.0
BuildRequires:    R-Matrix >= 1.2.13
BuildRequires:    R-CRAN-lme4 >= 1.1.8
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-nlme >= 3.1.124
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-pracma >= 2.1.4
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-bayesplot >= 1.5.0
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-rstantools >= 1.4.0
Requires:         R-Matrix >= 1.2.13
Requires:         R-CRAN-lme4 >= 1.1.8
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimates previously compiled stap regression models using the 'rstan'
package. Users specify models via a custom R syntax with a formula and
data.frame plus additional arguments for priors.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
