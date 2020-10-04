%global packname  spBFA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Bayesian Factor Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-msm >= 1.0.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.0
BuildRequires:    R-CRAN-pgdraw >= 1.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.500.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-msm >= 1.0.0
Requires:         R-CRAN-mvtnorm >= 1.0.0
Requires:         R-CRAN-pgdraw >= 1.0
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements a spatial Bayesian non-parametric factor analysis model with
inference in a Bayesian setting using Markov chain Monte Carlo (MCMC).
Spatial correlation is introduced in the columns of the factor loadings
matrix using a Bayesian non-parametric prior, the probit stick-breaking
process. Areal spatial data is modeled using a conditional autoregressive
(CAR) prior and point-referenced spatial data is treated using a Gaussian
process. The response variable can be modeled as Gaussian, probit, Tobit,
or Binomial (using Polya-Gamma augmentation). Temporal correlation is
introduced for the latent factors through a hierarchical structure and can
be specified as exponential or first-order autoregressive.

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
