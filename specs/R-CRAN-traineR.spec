%global packname  traineR
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive Models Homologator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.53
BuildRequires:    R-CRAN-nnet >= 7.3.12
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-CRAN-rpart >= 4.1.13
BuildRequires:    R-CRAN-ada >= 2.0.5
BuildRequires:    R-CRAN-e1071 >= 1.7.0.1
BuildRequires:    R-CRAN-dummies >= 1.5.6
BuildRequires:    R-CRAN-neuralnet >= 1.44.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-kknn >= 1.3.1
BuildRequires:    R-CRAN-xgboost >= 0.81.0.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-adabag 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-MASS >= 7.3.53
Requires:         R-CRAN-nnet >= 7.3.12
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-CRAN-rpart >= 4.1.13
Requires:         R-CRAN-ada >= 2.0.5
Requires:         R-CRAN-e1071 >= 1.7.0.1
Requires:         R-CRAN-dummies >= 1.5.6
Requires:         R-CRAN-neuralnet >= 1.44.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-kknn >= 1.3.1
Requires:         R-CRAN-xgboost >= 0.81.0.1
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-adabag 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 

%description
Methods to unify the different ways of creating predictive models and
their different predictive formats. It includes methods such as K-Nearest
Neighbors, Decision Trees, ADA Boosting, Extreme Gradient Boosting, Random
Forest, Neural Networks, Deep Learning, Support Vector Machines, Bayesian
Methods, Linear Discriminant Analysis and Quadratic Discriminant Analysis,
Logistic Regression, Penalized Logistic Regression.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
