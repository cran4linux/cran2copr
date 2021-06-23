%global __brp_check_rpaths %{nil}
%global packname  BSGW
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Survival Model with Lasso Shrinkage Using GeneralizedWeibull Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-MfUSampler 
BuildRequires:    R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-survival 
Requires:         R-CRAN-MfUSampler 
Requires:         R-methods 

%description
Bayesian survival model using Weibull regression on both scale and shape
parameters. Dependence of shape parameter on covariates permits deviation
from proportional-hazard assumption, leading to dynamic - i.e.
non-constant with time - hazard ratios between subjects. Bayesian Lasso
shrinkage in the form of two Laplace priors - one for scale and one for
shape coefficients - allows for many covariates to be included.
Cross-validation helper functions can be used to tune the shrinkage
parameters. Monte Carlo Markov Chain (MCMC) sampling using a Gibbs wrapper
around Radford Neal's univariate slice sampler (R package MfUSampler) is
used for coefficient estimation.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
