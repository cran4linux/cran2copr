%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  traineR
%global packver   2.2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.10
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive (Classification and Regression) Models Homologator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.53
BuildRequires:    R-CRAN-nnet >= 7.3.12
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-CRAN-rpart >= 4.1.13
BuildRequires:    R-CRAN-ada >= 2.0.5
BuildRequires:    R-CRAN-e1071 >= 1.7.0.1
BuildRequires:    R-CRAN-neuralnet >= 1.44.2
BuildRequires:    R-CRAN-kknn >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-xgboost >= 0.81.0.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-adabag 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-MASS >= 7.3.53
Requires:         R-CRAN-nnet >= 7.3.12
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-CRAN-rpart >= 4.1.13
Requires:         R-CRAN-ada >= 2.0.5
Requires:         R-CRAN-e1071 >= 1.7.0.1
Requires:         R-CRAN-neuralnet >= 1.44.2
Requires:         R-CRAN-kknn >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-xgboost >= 0.81.0.1
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-adabag 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-ggplot2 

%description
Methods to unify the different ways of creating predictive models and
their different predictive formats for classification and regression. It
includes methods such as K-Nearest Neighbors Schliep, K. P. (2004)
<doi:10.5282/ubm/epub.1769>, Decision Trees Leo Breiman, Jerome H.
Friedman, Richard A. Olshen, Charles J. Stone (2017)
<doi:10.1201/9781315139470>, ADA Boosting Esteban Alfaro, Matias Gamez,
Noelia García (2013) <doi:10.18637/jss.v054.i02>, Extreme Gradient
Boosting Chen & Guestrin (2016) <doi:10.1145/2939672.2939785>, Random
Forest Breiman (2001) <doi:10.1023/A:1010933404324>, Neural Networks
Venables, W. N., & Ripley, B. D. (2002) <ISBN:0-387-95457-0>, Support
Vector Machines Bennett, K. P. & Campbell, C. (2000)
<doi:10.1145/380995.380999>, Bayesian Methods Gelman, A., Carlin, J. B.,
Stern, H. S., & Rubin, D. B. (1995) <doi:10.1201/9780429258411>, Linear
Discriminant Analysis Venables, W. N., & Ripley, B. D. (2002)
<ISBN:0-387-95457-0>, Quadratic Discriminant Analysis Venables, W. N., &
Ripley, B. D. (2002) <ISBN:0-387-95457-0>, Logistic Regression Dobson, A.
J., & Barnett, A. G. (2018) <doi:10.1201/9781315182780> and Penalized
Logistic Regression Friedman, J. H., Hastie, T., & Tibshirani, R. (2010)
<doi:10.18637/jss.v033.i01>.

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
