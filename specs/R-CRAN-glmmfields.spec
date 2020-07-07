%global packname  glmmfields
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}
Summary:          Generalized Linear Mixed Models with Robust Random Fields forSpatiotemporal Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-rstan >= 2.18.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-methods 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-rstan >= 2.18.2
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-methods 
Requires:         R-cluster 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-assertthat 
Requires:         R-nlme 
Requires:         R-CRAN-forcats 

%description
Implements Bayesian spatial and spatiotemporal models that optionally
allow for extreme spatial deviations through time. 'glmmfields' uses a
predictive process approach with random fields implemented through a
multivariate-t distribution instead of the usual multivariate normal.
Sampling is conducted with 'Stan'. References: Anderson and Ward (2019)
<doi:10.1002/ecy.2403>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/test.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
