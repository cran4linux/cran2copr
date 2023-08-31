%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlearning
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Algorithms with Unified Interface and Confusion Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.4
Requires:         R-core >= 3.0.4
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-CRAN-rpart 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-class 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ipred 
Requires:         R-CRAN-rpart 

%description
A unified interface is provided to various machine learning algorithms
like linear or quadratic discriminant analysis, k-nearest neighbors,
random forest, support vector machine, ... It allows to train, test, and
apply cross-validation using similar functions and function arguments with
a minimalist and clean, formula-based interface. Missing data are
processed the same way as base and stats R functions for all algorithms,
both in training and testing. Confusion matrices are also provided with a
rich set of metrics calculated and a few specific plots.

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
