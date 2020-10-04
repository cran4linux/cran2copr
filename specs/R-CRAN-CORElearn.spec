%global packname  CORElearn
%global packver   1.54.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.54.2
Release:          3%{?dist}%{?buildtag}
Summary:          Classification, Regression and Feature Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-cluster 
BuildRequires:    R-rpart 
BuildRequires:    R-stats 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-rpart.plot 
Requires:         R-cluster 
Requires:         R-rpart 
Requires:         R-stats 
Requires:         R-nnet 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-rpart.plot 

%description
A suite of machine learning algorithms written in C++ with the R interface
contains several learning techniques for classification and regression.
Predictive models include e.g., classification and regression trees with
optional constructive induction and models in the leaves, random forests,
kNN, naive Bayes, and locally weighted regression. All predictions
obtained with these models can be explained and visualized with the
'ExplainPrediction' package. This package is especially strong in feature
evaluation where it contains several variants of Relief algorithm and many
impurity based attribute evaluation functions, e.g., Gini, information
gain, MDL, and DKM. These methods can be used for feature selection or
discretization of numeric attributes. The OrdEval algorithm and its
visualization is used for evaluation of data sets with ordinal features
and class, enabling analysis according to the Kano model of customer
satisfaction. Several algorithms support parallel multithreaded execution
via OpenMP. The top-level documentation is reachable through ?CORElearn.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
