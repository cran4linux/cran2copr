%global packname  rstanarm
%global packver   2.19.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.19.3
Release:          1%{?dist}
Summary:          Bayesian Applied Regression Modeling via Stan

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
Requires:         pandoc
Requires:         pandoc-citeproc
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-nlme >= 3.1.124
BuildRequires:    R-survival >= 2.40.1
BuildRequires:    R-CRAN-shinystan >= 2.3.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rstan >= 2.19.1
BuildRequires:    R-CRAN-StanHeaders >= 2.19.0
BuildRequires:    R-CRAN-loo >= 2.1.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.72.0.2
BuildRequires:    R-CRAN-bayesplot >= 1.7.0
BuildRequires:    R-Matrix >= 1.2.13
BuildRequires:    R-CRAN-lme4 >= 1.1.8
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-utils 
Requires:         R-nlme >= 3.1.124
Requires:         R-survival >= 2.40.1
Requires:         R-CRAN-shinystan >= 2.3.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rstan >= 2.19.1
Requires:         R-CRAN-loo >= 2.1.0
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-bayesplot >= 1.7.0
Requires:         R-Matrix >= 1.2.13
Requires:         R-CRAN-lme4 >= 1.1.8
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-RcppParallel 
Requires:         R-utils 

%description
Estimates previously compiled regression models using the 'rstan' package,
which provides the R interface to the Stan C++ library for Bayesian
estimation. Users specify models via the customary R syntax with a formula
and data.frame plus some additional arguments for priors.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
