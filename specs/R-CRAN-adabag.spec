%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adabag
%global packver   4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Applies Multiclass AdaBoost.M1, SAMME and Bagging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
It implements Freund and Schapire's Adaboost.M1 algorithm and Breiman's
Bagging algorithm using classification trees as individual classifiers.
Once these classifiers have been trained, they can be used to predict on
new data. Also, cross validation estimation of the error can be done.
Since version 2.0 the function margins() is available to calculate the
margins for these classifiers. Also a higher flexibility is achieved
giving access to the rpart.control() argument of 'rpart'. Four important
new features were introduced on version 3.0, AdaBoost-SAMME (Zhu et al.,
2009) is implemented and a new function errorevol() shows the error of the
ensembles as a function of the number of iterations. In addition, the
ensembles can be pruned using the option 'newmfinal' in the
predict.bagging() and predict.boosting() functions and the posterior
probability of each class for observations can be obtained. Version 3.1
modifies the relative importance measure to take into account the gain of
the Gini index given by a variable in each tree and the weights of these
trees. Version 4.0 includes the margin-based ordered aggregation for
Bagging pruning (Guo and Boukir, 2013) and a function to auto prune the
'rpart' tree. Moreover, three new plots are also available
importanceplot(), plot.errorevol() and plot.margins(). Version 4.1 allows
to predict on unlabeled data. Version 4.2 includes the parallel
computation option for some of the functions.

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
