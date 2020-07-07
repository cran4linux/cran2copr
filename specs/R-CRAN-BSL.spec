%global packname  BSL
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          3%{?dist}
Summary:          Bayesian Synthetic Likelihood

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-copula 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 

%description
Bayesian synthetic likelihood (BSL, Price et al. (2018)
<doi:10.1080/10618600.2017.1302882>) is an alternative to standard,
non-parametric approximate Bayesian computation (ABC). BSL assumes a
multivariate normal distribution for the summary statistic likelihood and
it is suitable when the distribution of the model summary statistics is
sufficiently regular. This package provides a Metropolis Hastings Markov
chain Monte Carlo implementation of three methods (BSL, uBSL and semiBSL)
and two shrinkage estimations (graphical lasso and Warton's estimation).
uBSL (Price et al. (2018) <doi:10.1080/10618600.2017.1302882>) uses an
unbiased estimator to the normal density. A semi-parametric version of BSL
(semiBSL, An et al. (2018) <arXiv:1809.05800>) is more robust to
non-normal summary statistics. Shrinkage estimations can help to bring
down the number of simulations when the dimension of the summary statistic
is high (e.g., BSLasso, An et al. (2019)
<doi:10.1080/10618600.2018.1537928>). Extensions to this package are
planned.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
