%global __brp_check_rpaths %{nil}
%global packname  LOGANTree
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tree-Based Models for the Analysis of Log Files from Computer-Based Assessments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-caretEnsemble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-stats 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-caretEnsemble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-gbm 
Requires:         R-stats 

%description
Enables researchers to model log-file data from computer-based assessments
using machine-learning techniques. It allows researchers to generate new
knowledge by comparing the performance of three tree-based classification
models (i.e., decision trees, random forest, and gradient boosting) to
predict student's outcome. It also contains a set of handful functions for
the analysis of the features' influence on the modeling. Data from the
Climate control item from the 2012 Programme for International Student
Assessment (PISA, <https://www.oecd.org/pisa/>) is available for an
illustration of the package's capability. He, Q., & von Davier, M. (2015)
<doi:10.1007/978-3-319-19977-1_13> Boehmke, B., & Greenwell, B. M. (2019)
<doi:10.1201/9780367816377> .

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
