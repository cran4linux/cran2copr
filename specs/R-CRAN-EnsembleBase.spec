%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EnsembleBase
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Extensible Package for Parallel, Batch Training of Base Learners for Ensemble Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-bartMachine 
Requires:         R-CRAN-kknn 
Requires:         R-methods 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-bartMachine 

%description
Extensible S4 classes and methods for batch training of regression and
classification algorithms such as Random Forest, Gradient Boosting
Machine, Neural Network, Support Vector Machines, K-Nearest Neighbors,
Penalized Regression (L1/L2), and Bayesian Additive Regression Trees.
These algorithms constitute a set of 'base learners', which can
subsequently be combined together to form ensemble predictions. This
package provides cross-validation wrappers to allow for downstream
application of ensemble integration techniques, including best-error
selection. All base learner estimation objects are retained, allowing for
repeated prediction calls without the need for re-training. For large
problems, an option is provided to save estimation objects to disk, along
with prediction methods that utilize these objects. This allows users to
train and predict with large ensembles of base learners without being
constrained by system RAM.

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
