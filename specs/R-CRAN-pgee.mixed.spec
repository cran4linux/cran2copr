%global packname  pgee.mixed
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Penalized Generalized Estimating Equations for Bivariate MixedOutcomes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods >= 3.3.2
BuildRequires:    R-CRAN-mvtnorm >= 1.0.5
BuildRequires:    R-CRAN-copula >= 0.999.15
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods >= 3.3.2
Requires:         R-CRAN-mvtnorm >= 1.0.5
Requires:         R-CRAN-copula >= 0.999.15
Requires:         R-CRAN-Rcpp >= 0.12.6

%description
Perform simultaneous estimation and variable selection for correlated
bivariate mixed outcomes (one continuous outcome and one binary outcome
per cluster) using penalized generalized estimating equations. In
addition, clustered Gaussian and binary outcomes can also be modeled. The
SCAD, MCP, and LASSO penalties are supported. Cross-validation can be
performed to find the optimal regularization parameter(s).

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
