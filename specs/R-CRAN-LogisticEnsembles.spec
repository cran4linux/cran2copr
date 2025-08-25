%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LogisticEnsembles
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatically Runs 36 Logistic Models (Individual and Ensembles)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-adabag 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-brnn 
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-MachineShop 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-reactablefmtr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tree 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-adabag 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-brnn 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-car 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-Cubist 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggplotify 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-ipred 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-MachineShop 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mda 
Requires:         R-parallel 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-reactablefmtr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tree 
Requires:         R-utils 
Requires:         R-CRAN-xgboost 

%description
Automatically returns 36 logistic models including 23 individual models
and 13 ensembles of models of logistic data. The package also returns 10
plots, 5 tables, and a summary report. The package automatically builds
all 36 models, reports all results, and provides graphics to show how the
models performed. This can be used for a wide range of data sets. The
package includes medical data (the Pima Indians data set), and information
about the performance of Lebron James. The package can be used to analyze
many other examples, such as stock market data. The package automatically
returns many values for each model, such as True Positive Rate, True
Negative Rate, False Positive Rate, False Negative Rate, Positive
Predictive Value, Negative Predictive Value, F1 Score, Area Under the
Curve. The package also returns 36 Receiver Operating Characteristic (ROC)
curves for each of the 36 models.

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
