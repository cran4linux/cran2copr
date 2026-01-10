%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  radiant.model
%global packver   1.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.9
Release:          1%{?dist}%{?buildtag}
Summary:          Model Menu for Radiant: Business Analytics using R and Shiny

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet >= 7.3.12
BuildRequires:    R-CRAN-rpart >= 4.1.11
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-sandwich >= 2.3.4
BuildRequires:    R-CRAN-car >= 2.1.3
BuildRequires:    R-CRAN-psych >= 1.8.4
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-lubridate >= 1.7.2
BuildRequires:    R-CRAN-e1071 >= 1.6.8
BuildRequires:    R-CRAN-radiant.data >= 1.6.6
BuildRequires:    R-CRAN-radiant.basics >= 1.6.6
BuildRequires:    R-CRAN-xgboost >= 1.6.0.1
BuildRequires:    R-CRAN-NeuralNetTools >= 1.5.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-stringr >= 1.1.0
BuildRequires:    R-CRAN-import >= 1.1.0
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.9
BuildRequires:    R-CRAN-patchwork >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-ggrepel >= 0.8
BuildRequires:    R-CRAN-data.tree >= 0.7.4
BuildRequires:    R-CRAN-broom >= 0.7.0
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-vip >= 0.3.2
BuildRequires:    R-CRAN-ranger >= 0.11.2
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-nnet >= 7.3.12
Requires:         R-CRAN-rpart >= 4.1.11
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-sandwich >= 2.3.4
Requires:         R-CRAN-car >= 2.1.3
Requires:         R-CRAN-psych >= 1.8.4
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-lubridate >= 1.7.2
Requires:         R-CRAN-e1071 >= 1.6.8
Requires:         R-CRAN-radiant.data >= 1.6.6
Requires:         R-CRAN-radiant.basics >= 1.6.6
Requires:         R-CRAN-xgboost >= 1.6.0.1
Requires:         R-CRAN-NeuralNetTools >= 1.5.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-stringr >= 1.1.0
Requires:         R-CRAN-import >= 1.1.0
Requires:         R-CRAN-DiagrammeR >= 1.0.9
Requires:         R-CRAN-patchwork >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-ggrepel >= 0.8
Requires:         R-CRAN-data.tree >= 0.7.4
Requires:         R-CRAN-broom >= 0.7.0
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-vip >= 0.3.2
Requires:         R-CRAN-ranger >= 0.11.2
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-yaml 

%description
The Radiant Model menu includes interfaces for linear and logistic
regression, naive Bayes, neural networks, classification and regression
trees, model evaluation, collaborative filtering, decision analysis, and
simulation. The application extends the functionality in 'radiant.data'.

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
