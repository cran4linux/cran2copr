%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MEMWAS
%global packver   0.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed-Effects Models with Autocorrelation Structures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits longitudinal mixed-effects models through a registered 'C++'
numerical backend. Supported serial covariance structures include
first-order autoregressive (AR(1)), exponential or Ornstein-Uhlenbeck,
higher-order autoregressive (AR(p)), first-order autoregressive
moving-average (ARMA(1,1)), compound symmetry, Toeplitz, and unstructured
covariance. Serial processes can be unified or attached independently to
numeric predictor loadings. Candidate temporal structures can be ranked on
a common sample by dependence-component grouped cross-validation, the
Akaike information criterion, the Bayesian information criterion, or
log-likelihood. Clustered, crossed, and nested random intercepts and
slopes are assembled jointly with diagonal or term-specific unstructured
covariance. Available approximation methods include Laplace, saddlepoint
likelihood with latent Laplace integration, adaptive Gaussian quadrature,
full-covariance Gaussian variational inference, and penalized
quasi-likelihood. Penalized smooth mean terms include ordinary and cyclic
P-splines, factor-by and varying-coefficient terms, tensor products,
shrinkage smooths, and whole-term selection. Term-specific penalties,
grouped fold-local smoothing selection, null-space constraints, and smooth
effective degrees of freedom remain separate from elastic-net coefficient
shrinkage while the smooth mean and serial covariance are fitted jointly.
Bootstrap resampling preserves the declared dependence components. The
mixed-effects framework is inspired by Laird and Ware (1982)
<doi:10.2307/2529876>; generalized-model approximations are inspired by
Breslow and Clayton (1993) <doi:10.1080/01621459.1993.10594284>; and
serial covariance formulations are inspired by Pinheiro and Bates (2000)
<doi:10.1007/b98882>. The run-time fitting interface imports no
third-party 'R' packages.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
