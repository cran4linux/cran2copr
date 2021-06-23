%global __brp_check_rpaths %{nil}
%global packname  HTLR
%global packver   0.4-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
