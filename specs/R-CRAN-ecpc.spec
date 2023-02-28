%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecpc
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Co-Data Learning for High-Dimensional Prediction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multiridge >= 1.5
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-gglasso 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-JOPS 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-multiridge >= 1.5
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-gglasso 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-JOPS 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-checkmate 

%description
Fit linear, logistic and Cox survival regression models penalised with
adaptive multi-group ridge penalties. The multi-group penalties correspond
to groups of covariates defined by (multiple) co-data sources. Group
hyperparameters are estimated with an empirical Bayes method of moments,
penalised with an extra level of hyper shrinkage. Various types of hyper
shrinkage may be used for various co-data. Co-data may be continuous or
categorical. The method accommodates inclusion of unpenalised covariates,
posterior selection of covariates and multiple data types. The model fit
is used to predict for new samples. The name 'ecpc' stands for Empirical
Bayes, Co-data learnt, Prediction and Covariate selection. See Van Nee et
al. (2020) <arXiv:2005.04010>.

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
