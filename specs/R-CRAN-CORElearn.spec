%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CORElearn
%global packver   1.57.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.57.2
Release:          1%{?dist}%{?buildtag}
Summary:          Classification, Regression and Feature Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-rpart.plot 
Requires:         R-CRAN-cluster 
Requires:         R-stats 
Requires:         R-CRAN-nnet 
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
