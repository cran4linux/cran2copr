%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pheble
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classifying High-Dimensional Phenotypes with Ensemble Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-adabag 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-evtree 
BuildRequires:    R-CRAN-frbs 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-CRAN-hda 
BuildRequires:    R-CRAN-HDclassif 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rpartScore 
BuildRequires:    R-CRAN-sparseLDA 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-themis 
BuildRequires:    R-utils 
Requires:         R-CRAN-adabag 
Requires:         R-base 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-evtree 
Requires:         R-CRAN-frbs 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-gmodels 
Requires:         R-CRAN-hda 
Requires:         R-CRAN-HDclassif 
Requires:         R-CRAN-ipred 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-kknn 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-MLmetrics 
Requires:         R-CRAN-nnet 
Requires:         R-parallel 
Requires:         R-CRAN-party 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rpartScore 
Requires:         R-CRAN-sparseLDA 
Requires:         R-stats 
Requires:         R-CRAN-themis 
Requires:         R-utils 

%description
A system for binary and multi-class classification of high-dimensional
phenotypic data using ensemble learning. By combining predictions from
different classification models, this package attempts to improve
performance over individual learners. The pre-processing, training,
validation, and testing are performed end-to-end to minimize user input
and simplify the process of classification.

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
