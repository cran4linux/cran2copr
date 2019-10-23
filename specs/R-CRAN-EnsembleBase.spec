%global packname  EnsembleBase
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Extensible Package for Parallel, Batch Training of Base Learnersfor Ensemble Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-bartMachine 
Requires:         R-CRAN-kknn 
Requires:         R-methods 
Requires:         R-CRAN-gbm 
Requires:         R-nnet 
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


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
