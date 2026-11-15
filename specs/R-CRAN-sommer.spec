%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sommer
%global packver   4.5.27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.27
Release:          1%{?dist}%{?buildtag}
Summary:          Solving Mixed Model Equations in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix >= 1.6.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-enhancer 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix >= 1.6.2
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-enhancer 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-crayon 

%description
Fits generalized linear and non linear mixed models with flexible
covariance structures for multiple random effects. Supports structured
random-effect and Gaussian residual covariances, including unstructured,
autoregressive, spatial, factor-analytic and reduced-rank models. These
structures can be combined using Kronecker products and user-defined
covariance functions. Known relationships among random-effect levels,
including pedigree and genomic relationship matrices, can be incorporated.
Gaussian models are fitted by maximum likelihood or restricted maximum
likelihood using complementary coefficient-space Henderson and
observation-space direct-inversion engines, with average-information
optimization and expectation-maximization recovery. Numerical methods
include sparse matrix factorization, preconditioned iterative solvers and
stochastic trace and log-determinant approximations for eligible
large-scale problems. Generalized models are fitted by penalized
quasi-likelihood or native Laplace-approximated maximum likelihood,
including joint models of responses from different families linked through
shared random effects. Provides prediction, uncertainty quantification and
inference tools for applications including quantitative genetics, genomic
prediction, multi-environment trials and spatial analysis
(Covarrubias-Pazaran, 2016 <doi:10.1371/journal.pone.0156744>; Maier et
al., 2015 <doi:10.1016/j.ajhg.2014.12.006>; Jensen et al., 1997).

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
