%global __brp_check_rpaths %{nil}
%global packname  psfmi
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prediction Model Pooling, Selection and Performance Evaluation Across Multiply Imputed Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 6.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-mice >= 3.12.0
BuildRequires:    R-CRAN-miceadds >= 3.10.28
BuildRequires:    R-CRAN-survival >= 3.1.12
BuildRequires:    R-CRAN-tibble >= 3.0.4
BuildRequires:    R-CRAN-car >= 3.0.10
BuildRequires:    R-CRAN-mitools >= 2.4
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-pROC >= 1.16.2
BuildRequires:    R-CRAN-lme4 >= 1.1.26
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-cvAUC >= 1.1.0
BuildRequires:    R-CRAN-norm >= 1.0.9.5
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-mitml >= 0.3.7
BuildRequires:    R-CRAN-ResourceSelection >= 0.3.5
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-rsample >= 0.0.8
Requires:         R-CRAN-rms >= 6.1.0
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-mice >= 3.12.0
Requires:         R-CRAN-miceadds >= 3.10.28
Requires:         R-CRAN-survival >= 3.1.12
Requires:         R-CRAN-tibble >= 3.0.4
Requires:         R-CRAN-car >= 3.0.10
Requires:         R-CRAN-mitools >= 2.4
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-pROC >= 1.16.2
Requires:         R-CRAN-lme4 >= 1.1.26
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-cvAUC >= 1.1.0
Requires:         R-CRAN-norm >= 1.0.9.5
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-mitml >= 0.3.7
Requires:         R-CRAN-ResourceSelection >= 0.3.5
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-rsample >= 0.0.8

%description
Pooling, backward and forward selection of linear, logistic and Cox
regression models in multiply imputed datasets. Backward and forward
selection can be done from the pooled model using Rubin's Rules (RR), the
D1, D2, D3, D4 and the median p-values method. This is also possible for
Mixed models. The models can contain continuous, dichotomous, categorical
and restricted cubic spline predictors and interaction terms between all
these type of predictors. The stability of the models can be evaluated
using bootstrapping and cluster bootstrapping. The package further
contains functions to pool the model performance as ROC/AUC, R-squares,
scaled Brier score, H&L test and calibration plots for logistic regression
models. Internal validation can be done with cross-validation or
bootstrapping. The adjusted intercept after shrinkage of pooled regression
coefficients can be obtained. Backward and forward selection as part of
internal validation is possible. A function to externally validate
logistic prediction models in multiple imputed datasets is available and a
function to compare models. Eekhout (2017)
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
