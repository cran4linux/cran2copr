%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ModTools
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Building Regression and Classification Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-relaimpo 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-NeuralNetTools 
BuildRequires:    R-CRAN-naivebayes 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-AER 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-pROC 
Requires:         R-methods 
Requires:         R-CRAN-relaimpo 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-car 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-class 
Requires:         R-CRAN-NeuralNetTools 
Requires:         R-CRAN-naivebayes 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-AER 

%description
Collection of tools for regression and classification tasks. The package
implements a consistent user interface to the most popular regression and
classification algorithms, such as random forest, neural networks, C5
trees and support vector machines, and complements it with a handful of
auxiliary functions, such as variable importance and a tuning function for
the parameters.

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
