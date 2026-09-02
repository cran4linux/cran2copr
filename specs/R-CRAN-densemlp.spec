%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  densemlp
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dense Neural Networks for Tabular Regression, Classification and Survival

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Dense feed-forward neural networks (multilayer perceptrons) for tabular
regression, classification and survival analysis, with a formula or x/y
interface. Supports residual and gated hidden blocks, batch normalization,
per-layer dropout, learned cross-feature interactions, exponential
moving-average weights, learning-rate schedules, internal bootstrap
ensembles and Adam optimization. Survival outcomes are trained with either
a batch-wise Breslow-tie Cox partial likelihood or a discrete-time
inverse-probability-of-censoring-weighted integrated Brier score. The
numerical kernels are implemented natively in C++ via 'RcppArmadillo',
with no external deep learning framework dependency (no 'torch' /
'libtorch'). Companion helpers provide k-fold cross-validation,
hyperparameter search and task-aware evaluation metrics.

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
