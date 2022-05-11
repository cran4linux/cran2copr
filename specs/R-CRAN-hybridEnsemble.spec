%global __brp_check_rpaths %{nil}
%global packname  hybridEnsemble
%global packver   1.7.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.8
Release:          1%{?dist}%{?buildtag}
Summary:          Build, Deploy and Evaluate Hybrid Ensembles

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-kernelFactory 
BuildRequires:    R-CRAN-ada 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-NMOF 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-Rmalschains 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-AUC 
BuildRequires:    R-CRAN-soma 
BuildRequires:    R-CRAN-genalg 
BuildRequires:    R-CRAN-reportr 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-tabuSearch 
BuildRequires:    R-CRAN-rotationForest 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-kernelFactory 
Requires:         R-CRAN-ada 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-NMOF 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-Rmalschains 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-AUC 
Requires:         R-CRAN-soma 
Requires:         R-CRAN-genalg 
Requires:         R-CRAN-reportr 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-tabuSearch 
Requires:         R-CRAN-rotationForest 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 

%description
Functions to build and deploy a hybrid ensemble consisting of different
sub-ensembles such as bagged logistic regressions, random forest,
stochastic boosting, kernel factory, bagged neural networks, bagged
support vector machines, rotation forest, bagged k-nearest neighbors, and
bagged naive Bayes. Functions to cross-validate the hybrid ensemble and
plot and summarize the results are also provided. There is also a function
to assess the importance of the predictors.

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
