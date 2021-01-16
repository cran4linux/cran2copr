%global packname  RaSEn
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random Subspace Ensemble Classification and Variable Screening

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-class 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rpart 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ranger 

%description
We propose a general ensemble classification framework, RaSE algorithm,
for the sparse classification problem. In RaSE algorithm, for each weak
learner, some random subspaces are generated and the optimal one is chosen
to train the model on the basis of some criterion. To be adapted to the
problem, a novel criterion, ratio information criterion (RIC) is put up
with based on Kullback-Leibler divergence. Besides minimizing RIC,
multiple criteria can be applied, for instance, minimizing extended
Bayesian information criterion (eBIC), minimizing training error,
minimizing the validation error, minimizing the cross-validation error,
minimizing leave-one-out error. There are various choices of base
classifier, for instance, linear discriminant analysis, quadratic
discriminant analysis, k-nearest neighbour, logistic regression, decision
trees, random forest, support vector machines. RaSE algorithm can also be
applied to do feature ranking, providing us the importance of each feature
based on the selected percentage in multiple subspaces. RaSE framework can
be extended to the general prediction framework, including both
classification and regression. We can use the selected percentages of
variables for variable screening. The latest version added the variable
screening function available for both regression and classification.

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
