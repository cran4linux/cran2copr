%global packname  EZtune
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tunes AdaBoost, Elastic Net, Support Vector Machines, and Gradient Boosting Machines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ada 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ROCR 
Requires:         R-CRAN-ada 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ROCR 

%description
Contains two functions that are intended to make tuning supervised
learning methods easy. The eztune function uses a genetic algorithm or
Hooke-Jeeves optimizer to find the best set of tuning parameters. The user
can choose the optimizer, the learning method, and if optimization will be
based on accuracy obtained through validation error, cross validation, or
resubstitution. The function eztune.cv will compute a cross validated
error rate. The purpose of eztune_cv is to provide a cross validated
accuracy or MSE when resubstitution or validation data are used for
optimization because error measures from both approaches can be
misleading.

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
