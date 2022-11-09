%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  planningML
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Sample Size Calculator for Machine Learning Applications in Healthcare

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MESS 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-stats 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MESS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-pROC 
Requires:         R-stats 

%description
Advances in automated document classification has led to identifying
massive numbers of clinical concepts from handwritten clinical notes.
These high dimensional clinical concepts can serve as highly informative
predictors in building classification algorithms for identifying patients
with different clinical conditions, commonly referred to as patient
phenotyping. However, from a planning perspective, it is critical to
ensure that enough data is available for the phenotyping algorithm to
obtain a desired classification performance. This challenge in sample size
planning is further exacerbated by the high dimension of the feature space
and the inherent imbalance of the response class. Currently available
sample size planning methods can be categorized into: (i) model-based
approaches that predict the sample size required for achieving a desired
accuracy using a linear machine learning classifier and (ii) learning
curve-based approaches (Figueroa et al. (2012)
<doi:10.1186/1472-6947-12-8>) that fit an inverse power law curve to pilot
data to extrapolate performance. We develop model-based approaches for
imbalanced data with correlated features, deriving sample size formulas
for performance metrics that are sensitive to class imbalance such as Area
Under the receiver operating characteristic Curve (AUC) and Matthews
Correlation Coefficient (MCC). This is done using a two-step approach
where we first perform feature selection using the innovated High
Criticism thresholding method (Hall and Jin (2010)
<doi:10.1214/09-AOS764>), then determine the sample size by optimizing the
two performance metrics. Further, we develop software in the form of an R
package named 'planningML' and an 'R' 'Shiny' app to facilitate the
convenient implementation of the developed model-based approaches and
learning curve approaches for imbalanced data. We apply our methods to the
problem of phenotyping rare outcomes using the MIMIC-III electronic health
record database. We show that our developed methods which relate training
data size and performance on AUC and MCC, can predict the true or observed
performance from linear ML classifiers such as LASSO and SVM at different
training data sizes. Therefore, in high-dimensional classification
analysis with imbalanced data and correlated features, our approach can
efficiently and accurately determine the sample size needed for
machine-learning based classification.

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
