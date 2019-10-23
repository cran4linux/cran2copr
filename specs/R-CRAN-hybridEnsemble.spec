%global packname  hybridEnsemble
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
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
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-nnet 
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
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-kernelFactory 
Requires:         R-CRAN-ada 
Requires:         R-rpart 
Requires:         R-CRAN-ROCR 
Requires:         R-nnet 
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

%description
Functions to build and deploy a hybrid ensemble consisting of eight
different sub-ensembles: bagged logistic regressions, random forest,
stochastic boosting, kernel factory, bagged neural networks, bagged
support vector machines, rotation forest, and bagged k-nearest neighbors.
Functions to cross-validate the hybrid ensemble and plot and summarize the
results are also provided. There is also a function to assess the
importance of the predictors.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
