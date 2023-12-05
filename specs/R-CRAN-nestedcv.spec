%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nestedcv
%global packver   0.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Nested Cross-Validation with 'glmnet' and 'caret'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-matrixTests 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-matrixTests 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-rlang 

%description
Implements nested k*l-fold cross-validation for lasso and elastic-net
regularised linear models via the 'glmnet' package and other machine
learning models via the 'caret' package. Cross-validation of 'glmnet'
alpha mixing parameter and embedded fast filter functions for feature
selection are provided. Described as double cross-validation by Stone
(1977) <doi:10.1111/j.2517-6161.1977.tb01603.x>. Also implemented is a
method using outer CV to measure unbiased model performance metrics when
fitting Bayesian linear and logistic regression shrinkage models using the
horseshoe prior over parameters to encourage a sparse model as described
by Piironen & Vehtari (2017) <doi:10.1214/17-EJS1337SI>.

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
