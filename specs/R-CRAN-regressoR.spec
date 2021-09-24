%global __brp_check_rpaths %{nil}
%global packname  regressoR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Data Analysis System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-CRAN-rpart >= 4.1.13
BuildRequires:    R-CRAN-pls >= 2.7.1
BuildRequires:    R-CRAN-gbm >= 2.1.5
BuildRequires:    R-CRAN-glmnet >= 2.0.16
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0.0
BuildRequires:    R-CRAN-e1071 >= 1.7.0.1
BuildRequires:    R-CRAN-neuralnet >= 1.44.2
BuildRequires:    R-CRAN-shiny >= 1.2.0
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-shinycustomloader >= 0.9.0
BuildRequires:    R-CRAN-shinydashboard >= 0.7.1
BuildRequires:    R-CRAN-DT >= 0.5
BuildRequires:    R-CRAN-echarts4r >= 0.4.1
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-shinyAce >= 0.3.3
BuildRequires:    R-CRAN-golem >= 0.3.1
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-CRAN-rpart.plot 
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-CRAN-rpart >= 4.1.13
Requires:         R-CRAN-pls >= 2.7.1
Requires:         R-CRAN-gbm >= 2.1.5
Requires:         R-CRAN-glmnet >= 2.0.16
Requires:         R-CRAN-shinydashboardPlus >= 2.0.0
Requires:         R-CRAN-e1071 >= 1.7.0.1
Requires:         R-CRAN-neuralnet >= 1.44.2
Requires:         R-CRAN-shiny >= 1.2.0
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-shinycustomloader >= 0.9.0
Requires:         R-CRAN-shinydashboard >= 0.7.1
Requires:         R-CRAN-DT >= 0.5
Requires:         R-CRAN-echarts4r >= 0.4.1
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-shinyAce >= 0.3.3
Requires:         R-CRAN-golem >= 0.3.1
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-kknn 
Requires:         R-CRAN-rpart.plot 

%description
Perform a supervised data analysis on a database through a 'shiny'
graphical interface. It includes methods such as linear regression,
penalized regression, k-nearest neighbors, decision trees, ada boosting,
extreme gradient boosting, random forest, neural networks, deep learning
and support vector machines.

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
