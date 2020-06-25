%global packname  BGVAR
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Bayesian Global Vector Autoregressions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bayesm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stochvol 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bayesm 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-GIGrvg 
Requires:         R-graphics 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-stochvol 
Requires:         R-utils 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Estimation of Bayesian Global Vector Autoregressions (BGVAR) with
different prior setups and the possibility to introduce stochastic
volatility. Built-in priors include the Minnesota, the stochastic search
variable selection and Normal-Gamma (NG) prior. For a reference see also
Crespo Cuaresma, J., Feldkircher, M. and F. Huber (2016) "Forecasting with
Global Vector Autoregressive Models: a Bayesian Approach", Journal of
Applied Econometrics, Vol. 31(7), pp. 1371-1391 <doi:10.1002/jae.2504>.
Post-processing functions allow for doing predictions, structurally
identify the model with short-run or sign-restrictions and compute impulse
response functions, historical decompositions and forecast error variance
decompositions. Plotting functions are also available.

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

%files
%{rlibdir}/%{packname}
