%global packname  mikropml
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          User-Friendly R Package for Supervised Machine Learning Pipelines

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-MLmetrics 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xgboost 

%description
An interface to build machine learning models for classification and
regression problems. 'mikropml' implements the ML pipeline described by
Topçuoğlu et al. (2020) <doi:10.1128/mBio.00434-20> with reasonable
default options for data preprocessing, hyperparameter tuning,
cross-validation, testing, model evaluation, and interpretation steps. See
the website <http://www.schlosslab.org/mikropml/> for more information,
documentation, and examples.

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
