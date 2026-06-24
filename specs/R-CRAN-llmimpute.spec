%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  llmimpute
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Missing Data Imputation via Language Models and Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-methods 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-methods 

%description
Provides missing data imputation through two complementary engines: a
large language model engine that communicates with the 'Anthropic'
'Claude' application programming interface for context-aware semantic
imputation, and a fully self-contained offline engine implementing
nineteen statistical and machine learning algorithms entirely in base R
with no additional package dependencies. Offline methods include mean,
median, mode, last observation carried forward, next observation carried
backward, hot-deck, predictive mean matching, k-nearest neighbours,
ordinary least-squares regression, Lasso with coordinate descent, Ridge
with closed-form solution, Bayesian Ridge regression with evidence
approximation following MacKay (1992), support vector regression with a
radial basis function kernel, classification and regression trees, random
forests, gradient boosting, iterative random forest imputation, principal
component analysis imputation via iterative singular value decomposition,
and nuclear-norm minimisation via singular value thresholding. When no API
key is available the package automatically falls back to the offline
engine, ensuring full operation in environments without internet access.
Every imputed value is accompanied by a confidence score and a
plain-language reasoning string, producing reproducible audit trails. The
automatic method selector chooses the best algorithm per column based on
data type, skewness, missingness rate, and inter-column correlations.

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
