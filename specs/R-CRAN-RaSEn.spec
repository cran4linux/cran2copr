%global packname  RaSEn
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Random Subspace Ensemble Classification

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-rpart 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-formatR 
Requires:         R-MASS 
Requires:         R-CRAN-caret 
Requires:         R-class 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-foreach 
Requires:         R-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-rpart 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-formatR 

%description
We propose a new model-free ensemble classification framework, RaSE
algorithm, for the sparse classification problem. In RaSE algorithm, for
each weak learner, some random subspaces are generated and the optimal one
is chosen to train the model on the basis of some criterion. To be adapted
to the problem, a novel criterion, ratio information criterion (RIC) is
put up with based on Kullback-Leibler divergence. Besides minimizing RIC,
multiple criteria can be applied, for instance, minimizing extended
Bayesian information criterion (eBIC), minimizing training error,
minimizing the validation error, minimizing the cross-validation error,
minimizing leave-one-out error. And the choices of base classifiers are
also various, for instance, linear discriminant analysis, quadratic
discriminant analysis, k-nearest neighbour, logistic regression, decision
trees, random forest, support vector machines. RaSE algorithm can also be
applied to do feature ranking, providing us the importance of each feature
based on the selected percentage in multiple subspaces.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
