%global packname  creditmodel
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Toolkit for Credit Modeling, Analysis and Visualization

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-xgboost 

%description
Provides a highly efficient R tool suite for Credit Modeling, Analysis and
Visualization.Contains infrastructure functionalities such as data
exploration and preparation, missing values treatment, outliers treatment,
variable derivation, variable selection, dimensionality reduction, grid
search for hyper parameters, data mining and visualization, model
evaluation, strategy analysis etc. This package is designed to make the
development of binary classification models (machine learning based models
as well as credit scorecard) simpler and faster. The references including:
1 Refaat, M. (2011, ISBN: 9781447511199). Credit Risk Scorecard:
Development and Implementation Using SAS; 2 Bezdek, James C.FCM: The fuzzy
c-means clustering algorithm. Computers & Geosciences
(0098-3004),<DOI:10.1016/0098-3004(84)90020-7>.

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
