%global __brp_check_rpaths %{nil}
%global packname  NADIA
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          NA Data Imputation Algorithms

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-mlr3pipelines 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-mlr3learners 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-missMDA 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-CRAN-softImpute 
BuildRequires:    R-CRAN-missRanger 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-mlr3pipelines 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-mlr3learners 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-missMDA 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-VIM 
Requires:         R-CRAN-softImpute 
Requires:         R-CRAN-missRanger 
Requires:         R-methods 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmnet 

%description
Creates a uniform interface for several advanced imputations missing data
methods. Every available method can be used as a part of 'mlr3' pipelines
which allows easy tuning and performance evaluation. Most of the used
functions work separately on the training and test sets (imputation is
trained on the training set and impute training data. After that
imputation is again trained on the test set and impute test data).

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
