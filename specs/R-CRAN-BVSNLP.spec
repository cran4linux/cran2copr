%global packname  BVSNLP
%global packver   1.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          2%{?dist}
Summary:          Bayesian Variable Selection in High Dimensional Settings usingNonlocal Priors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppNumerical 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 

%description
Variable/Feature selection in high or ultra-high dimensional settings has
gained a lot of attention recently specially in cancer genomic studies.
This package provides a Bayesian approach to tackle this problem, where it
exploits mixture of point masses at zero and nonlocal priors to improve
the performance of variable selection and coefficient estimation. product
moment (pMOM) and product inverse moment (piMOM) nonlocal priors are
implemented and can be used for the analyses. This package performs
variable selection for binary response and survival time response datasets
which are widely used in biostatistic and bioinformatics community.
Benefiting from parallel computing ability, it reports necessary outcomes
of Bayesian variable selection such as Highest Posterior Probability Model
(HPPM), Median Probability Model (MPM) and posterior inclusion probability
for each of the covariates in the model. The option to use Bayesian Model
Averaging (BMA) is also part of this package that can be exploited for
predictive power measurements in real datasets.

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
%{rlibdir}/%{packname}/libs
