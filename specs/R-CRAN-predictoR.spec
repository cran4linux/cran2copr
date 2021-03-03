%global packname  predictoR
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive Data Analysis System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rattle >= 5.2.0
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-CRAN-rpart >= 4.1.13
BuildRequires:    R-CRAN-ada >= 2.0.5
BuildRequires:    R-CRAN-glmnet >= 2.0.16
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-e1071 >= 1.7.0.1
BuildRequires:    R-CRAN-neuralnet >= 1.44.2
BuildRequires:    R-CRAN-kknn >= 1.3.1
BuildRequires:    R-CRAN-tidyverse >= 1.2.1
BuildRequires:    R-CRAN-shiny >= 1.2.0
BuildRequires:    R-CRAN-ROCR >= 1.0.7
BuildRequires:    R-CRAN-zip >= 1.0.0
BuildRequires:    R-CRAN-shinyjs >= 1.0
BuildRequires:    R-CRAN-colourpicker >= 1.0
BuildRequires:    R-CRAN-corrplot >= 0.84
BuildRequires:    R-CRAN-xgboost >= 0.81.0.1
BuildRequires:    R-CRAN-shinydashboardPlus >= 0.6.0
BuildRequires:    R-CRAN-flexdashboard >= 0.5.1.1
BuildRequires:    R-CRAN-DT >= 0.5
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.4
BuildRequires:    R-CRAN-shinyAce >= 0.3.3
Requires:         R-CRAN-rattle >= 5.2.0
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-CRAN-rpart >= 4.1.13
Requires:         R-CRAN-ada >= 2.0.5
Requires:         R-CRAN-glmnet >= 2.0.16
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-e1071 >= 1.7.0.1
Requires:         R-CRAN-neuralnet >= 1.44.2
Requires:         R-CRAN-kknn >= 1.3.1
Requires:         R-CRAN-tidyverse >= 1.2.1
Requires:         R-CRAN-shiny >= 1.2.0
Requires:         R-CRAN-ROCR >= 1.0.7
Requires:         R-CRAN-zip >= 1.0.0
Requires:         R-CRAN-shinyjs >= 1.0
Requires:         R-CRAN-colourpicker >= 1.0
Requires:         R-CRAN-corrplot >= 0.84
Requires:         R-CRAN-xgboost >= 0.81.0.1
Requires:         R-CRAN-shinydashboardPlus >= 0.6.0
Requires:         R-CRAN-flexdashboard >= 0.5.1.1
Requires:         R-CRAN-DT >= 0.5
Requires:         R-CRAN-shinyWidgets >= 0.4.4
Requires:         R-CRAN-shinyAce >= 0.3.3

%description
Perform a supervised data analysis on a database through a 'shiny'
graphical interface. It includes methods such as K-Nearest Neighbors,
Decision Trees, ADA Boosting, Extreme Gradient Boosting, Random Forest,
Neural Networks, Deep Learning, Support Vector Machines and Bayesian
Methods.

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
