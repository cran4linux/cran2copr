%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  healthcareai
%global packver   2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Healthcare Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.81
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-ranger >= 0.8.0
BuildRequires:    R-CRAN-recipes >= 0.1.3.9002
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-caret >= 6.0.81
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-ranger >= 0.8.0
Requires:         R-CRAN-recipes >= 0.1.3.9002
Requires:         R-methods 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-MLmetrics 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xgboost 

%description
Aims to make machine learning in healthcare as easy as possible. You can
develop customized, reliable, high-performance machine learning models
with minimal code. Models are created with automatic preprocessing,
hyperparameter tuning, and algorithm selection (between 'xgboost' Chen, T.
& Guestrin, C. (2016) <arXiv:1603.02754>, 'ranger' Wright, M. N., &
Ziegler, A. (2017) <doi:10.18637/jss.v077.i01>, and 'glm' Friedman J,
Hastie T, Tibshirani R. (2010) <doi:10.18637/jss.v033.i01>) so that they
can be easily put into production. Additionally, there are tools to help
understand how a model makes its predictions, select prediction
threshholds for operational use, and evaluate model performance over time.
Code uses 'tidyverse' syntax and most methods have an associated
visualization.

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
