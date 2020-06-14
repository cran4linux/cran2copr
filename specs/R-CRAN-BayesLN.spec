%global packname  BayesLN
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Bayesian Inference for Log-Normal Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-ghyp 
BuildRequires:    R-CRAN-fAsianOptions 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-ghyp 
Requires:         R-CRAN-fAsianOptions 
Requires:         R-CRAN-coda 
Requires:         R-MASS 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-data.table 

%description
Bayesian inference under log-normality assumption must be performed very
carefully. In fact, under the common priors for the variance, useful
quantities in the original data scale (like mean and quantiles) do not
have posterior moments that are finite (Fabrizi et al. 2012
<doi:10.1214/12-BA733>). This package allows to easily carry out a proper
Bayesian inferential procedure by fixing a suitable distribution (the
generalized inverse Gaussian) as prior for the variance. Functions to
estimate several kind of means (unconditional, conditional and conditional
under a mixed model) and quantiles (unconditional and conditional) are
provided.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
