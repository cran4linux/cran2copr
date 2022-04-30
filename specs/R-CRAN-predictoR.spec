%global __brp_check_rpaths %{nil}
%global packname  predictoR
%global packver   2.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive Data Analysis System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 4.1.2
BuildRequires:    R-CRAN-rpart >= 4.1.15
BuildRequires:    R-CRAN-rpart.plot >= 3.0.9
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0.3
BuildRequires:    R-CRAN-shinyjs >= 2.0.0
BuildRequires:    R-CRAN-xtable >= 1.8.4
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-traineR >= 1.6.2
BuildRequires:    R-CRAN-xgboost >= 1.4.1.1
BuildRequires:    R-CRAN-colourpicker >= 1.1.1
BuildRequires:    R-CRAN-shinycustomloader >= 0.9.0
BuildRequires:    R-CRAN-shinydashboard >= 0.7.2
BuildRequires:    R-CRAN-htmltools >= 0.5.2
BuildRequires:    R-CRAN-echarts4r >= 0.4.2
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-shinyAce >= 0.4.1
BuildRequires:    R-CRAN-golem >= 0.3.1
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-CRAN-DT >= 0.19
Requires:         R-CRAN-glmnet >= 4.1.2
Requires:         R-CRAN-rpart >= 4.1.15
Requires:         R-CRAN-rpart.plot >= 3.0.9
Requires:         R-CRAN-shinydashboardPlus >= 2.0.3
Requires:         R-CRAN-shinyjs >= 2.0.0
Requires:         R-CRAN-xtable >= 1.8.4
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-traineR >= 1.6.2
Requires:         R-CRAN-xgboost >= 1.4.1.1
Requires:         R-CRAN-colourpicker >= 1.1.1
Requires:         R-CRAN-shinycustomloader >= 0.9.0
Requires:         R-CRAN-shinydashboard >= 0.7.2
Requires:         R-CRAN-htmltools >= 0.5.2
Requires:         R-CRAN-echarts4r >= 0.4.2
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-shinyAce >= 0.4.1
Requires:         R-CRAN-golem >= 0.3.1
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-CRAN-DT >= 0.19

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
