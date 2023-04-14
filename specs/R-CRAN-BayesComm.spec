%global __brp_check_rpaths %{nil}
%global packname  BayesComm
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Community Ecology Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.6
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.6
Requires:         R-CRAN-abind 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mvtnorm 

%description
Bayesian multivariate binary (probit) regression models for analysis of
ecological communities.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
