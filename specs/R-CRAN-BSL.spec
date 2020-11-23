%global packname  BSL
%global packver   3.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Synthetic Likelihood

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-whitening 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-whitening 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-doRNG 
Requires:         R-methods 
Requires:         R-CRAN-stringr 

%description
Bayesian synthetic likelihood (BSL, Price et al. (2018)
<doi:10.1080/10618600.2017.1302882>) is an alternative to standard,
non-parametric approximate Bayesian computation (ABC). BSL assumes a
multivariate normal distribution for the summary statistic likelihood and
it is suitable when the distribution of the model summary statistics is
sufficiently regular. This package provides a Metropolis Hastings Markov
chain Monte Carlo implementation of four methods (BSL, uBSL, semiBSL and
BSLmisspec) and two shrinkage estimators (graphical lasso and Warton's
estimator). uBSL (Price et al. (2018) <doi:10.1080/10618600.2017.1302882>)
uses an unbiased estimator to the normal density. A semi-parametric
version of BSL (semiBSL, An et al. (2018) <arXiv:1809.05800>) is more
robust to non-normal summary statistics. BSLmisspec (Frazier et al. 2019
<arXiv:1904.04551>) estimates the Gaussian synthetic likelihood whilst
acknowledging that there may be incompatibility between the model and the
observed summary statistic. Shrinkage estimation can help to decrease the
number of model simulations when the dimension of the summary statistic is
high (e.g., BSLasso, An et al. (2019)
<doi:10.1080/10618600.2018.1537928>). Extensions to this package are
planned.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
