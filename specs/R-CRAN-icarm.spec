%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  icarm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interpretable Contextual-Accountable and Responsible Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 

%description
A general-purpose framework for Interpretable Contextual-Accountable and
Responsible Machine Learning (ICARM) that works with any clean tabular
data across any application domain including healthcare, finance, social
science, business, and education. Automatically detects whether a
prediction task is binary classification, multi-class classification, or
regression from the target variable type. Provides a unified entry point
icarm_fit() supporting both interpretable learners (Classification and
Regression Trees (CART), logistic regression, linear regression,
Generalized Additive Models (GAM)) and extended learners (random forest,
'XGBoost', Support Vector Machines (SVM)) with consistent interfaces for
global and local model explanation including approximate SHapley Additive
exPlanations (SHAP) values and Partial Dependence Profiles (PDPs),
learning curve diagnostics, group-level fairness auditing across protected
attributes, probability calibration, threshold analysis, multi-model
comparison, reproducible JavaScript Object Notation (JSON) audit trails,
and accountability scorecards. The contextual accountability framing
emphasises that algorithmic fairness and interpretability requirements
depend on the deployment domain and must be evaluated accordingly. Extends
the 'civic.icarm' framework (Awe 2025)
<https://cran.r-project.org/package=civic.icarm> to general-purpose
applications beyond civic and political education.

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
