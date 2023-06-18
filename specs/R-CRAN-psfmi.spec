%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psfmi
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prediction Model Pooling, Selection and Performance Evaluation Across Multiply Imputed Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-norm 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-mitools 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-mitml 
BuildRequires:    R-CRAN-cvAUC 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-norm 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-mitools 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-mitml 
Requires:         R-CRAN-cvAUC 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-car 

%description
Pooling, backward and forward selection of linear, logistic and Cox
regression models in multiply imputed datasets. Backward and forward
selection can be done from the pooled model using Rubin's Rules (RR), the
D1, D2, D3, D4 and the median p-values method. This is also possible for
Mixed models. The models can contain continuous, dichotomous, categorical
and restricted cubic spline predictors and interaction terms between all
these type of predictors. The stability of the models can be evaluated
using (cluster) bootstrapping. The package further contains functions to
pool model performance measures as ROC/AUC, Reclassification, R-squared,
scaled Brier score, H&L test and calibration plots for logistic regression
models. Internal validation can be done across multiply imputed datasets
with cross-validation or bootstrapping. The adjusted intercept after
shrinkage of pooled regression coefficients can be obtained. Backward and
forward selection as part of internal validation is possible. A function
to externally validate logistic prediction models in multiple imputed
datasets is available and a function to compare models. For Cox models a
strata variable can be included. Eekhout (2017)
<doi:10.1186/s12874-017-0404-7>. Wiel (2009)
<doi:10.1093/biostatistics/kxp011>. Marshall (2009)
<doi:10.1186/1471-2288-9-57>.

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
