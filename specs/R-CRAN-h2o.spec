%global packname  h2o
%global packver   3.32.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.32.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface for the 'H2O' Scalable Machine Learning Platform

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz
Source1:          https://s3.amazonaws.com/h2o-release/h2o/rel-zipf/3/Rjar/h2o.jar

Requires:         java
BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-jsonlite 

%description
R interface for 'H2O', the scalable open source machine learning platform
that offers parallelized implementations of many supervised and
unsupervised machine learning algorithms such as Generalized Linear Models
(GLM), Gradient Boosting Machines (including XGBoost), Random Forests,
Deep Neural Networks (Deep Learning), Stacked Ensembles, Naive Bayes,
Generalized Additive Models (GAM), Cox Proportional Hazards, K-Means, PCA,
Word2Vec, as well as a fully automatic machine learning algorithm (H2O
AutoML).

%prep
%setup -q -c -n %{packname}
cp %{SOURCE1} %{packname}/inst/java
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
