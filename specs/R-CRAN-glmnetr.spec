%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmnetr
%global packver   0.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nested Cross Validation for the Relaxed Lasso and Other Machine Learning Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-smoof 
BuildRequires:    R-CRAN-mlrMBO 
BuildRequires:    R-CRAN-ParamHelpers 
BuildRequires:    R-CRAN-torch 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-smoof 
Requires:         R-CRAN-mlrMBO 
Requires:         R-CRAN-ParamHelpers 
Requires:         R-CRAN-torch 

%description
Cross validation informed Relaxed LASSO, Artificial Neural Network (ANN),
gradient boosting machine ('xgboost'), Recursive Partitioning ('RPART') or
step wise regression models are fit.  It fits all these model as
extensions of linear, logistic and Cox regression models.  The package can
fit all these models in a single call, and performs nested cross
validation allowing the user to evaluate and compare the performances of
these different models.  The package fits these models using other
packages including 'glmnet', 'survival', 'xgboost', 'rpart' and 'torch'.
For the relaxed lasso models 'glmnetr' uses 'stat' and 'survival' to
obtain stable model fits, and obtain these often more quickly.  This too
might be achieved using the 'path=TRUE' option in 'glmnet'. While the
package fits nested cross validation for the lasso and other models, it
does not fit the general elastic net model.  If you are fitting not a
relaxed lasso model but an elastic-net model, then the R-packages
'nestedcv' <https://cran.r-project.org/package=nestedcv>, 'glmnetSE'
<https://cran.r-project.org/package=glmnetSE> or others may provide
greater functionality when performing a nested CV. As with the 'glmnet'
package, this package passes most relevant information to the output
object which can be evaluated using plot, summary() and predict()
functions.  The 'glmnetr' package has some features and functionality that
we find useful, but omits some of the functionality of 'glmnet' as well.
Use of the 'glmnetr' package has many similarities to the 'glmnet' package
and it is recommended that the user of 'glmnetr' first become familiar
with the 'glmnet' package <https://cran.r-project.org/package=glmnet>,
with the "An Introduction to glmnet" and "The Relaxed Lasso" being
especially helpful in this regard.

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
