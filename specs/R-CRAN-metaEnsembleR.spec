%global __brp_check_rpaths %{nil}
%global packname  metaEnsembleR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Intuitive Package for Meta-Ensemble Learning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-randomForest 

%description
Extends the base classes and methods of 'caret' package for integration of
base learners. The user can input the number of different base learners,
and specify the final learner, along with the train-validation-test data
partition split ratio. The predictions on the unseen new data is the
resultant of the ensemble meta-learning
<https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/>
of the heterogeneous learners aimed to reduce the generalization error in
the predictive models. It significantly lowers the barrier for the
practitioners to apply heterogeneous ensemble learning techniques in an
amateur fashion to their everyday predictive problems.

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
