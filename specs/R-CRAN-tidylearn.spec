%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidylearn
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Unified Tidy Interface to R's Machine Learning Ecosystem

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-cluster >= 2.1.0
BuildRequires:    R-CRAN-smacof >= 2.1.0
BuildRequires:    R-CRAN-dbscan >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-cluster >= 2.1.0
Requires:         R-CRAN-smacof >= 2.1.0
Requires:         R-CRAN-dbscan >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-MASS 

%description
Provides a unified tidyverse-compatible interface to R's machine learning
packages. Wraps established implementations from 'glmnet', 'randomForest',
'xgboost', 'e1071', 'rpart', 'gbm', 'nnet', 'cluster', 'dbscan', and
others - providing consistent function signatures, tidy tibble output, and
unified 'ggplot2'-based visualization. The underlying algorithms are
unchanged; 'tidylearn' simply makes them easier to use together. Access
raw model objects via the $fit slot for package-specific functionality.
Methods include random forests Breiman (2001)
<doi:10.1023/A:1010933404324>, LASSO regression Tibshirani (1996)
<doi:10.1111/j.2517-6161.1996.tb02080.x>, elastic net Zou and Hastie
(2005) <doi:10.1111/j.1467-9868.2005.00503.x>, support vector machines
Cortes and Vapnik (1995) <doi:10.1007/BF00994018>, and gradient boosting
Friedman (2001) <doi:10.1214/aos/1013203451>.

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
