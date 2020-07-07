%global packname  HTLR
%global packver   0.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}
Summary:          Bayesian Logistic Regression with Heavy-Tailed Priors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-BCBCSF 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-BCBCSF 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-magrittr 

%description
Efficient Bayesian multinomial logistic regression based on heavy-tailed
(hyper-LASSO, non-convex) priors. The posterior of coefficients and
hyper-parameters is sampled with restricted Gibbs sampling for leveraging
the high-dimensionality and Hamiltonian Monte Carlo for handling the
high-correlation among coefficients. A detailed description of the method:
Li and Yao (2018), Journal of Statistical Computation and Simulation,
88:14, 2827-2851, <arXiv:1405.3319>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/install_old_htlr.sh
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
