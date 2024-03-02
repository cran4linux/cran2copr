%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  csmpv
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Biomarker Confirmation, Selection, Modelling, Prediction, and Validation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-forestmodel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-forestmodel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Matrix 

%description
There are diverse purposes such as biomarker confirmation, novel biomarker
discovery, constructing predictive models, model-based prediction, and
validation. It handles binary, continuous, and time-to-event outcomes at
the sample or patient level. - Biomarker confirmation utilizes established
functions like glm() from 'stats', coxph() from 'survival', surv_fit(),
and ggsurvplot() from 'survminer'. - Biomarker discovery and variable
selection are facilitated by three LASSO-related functions LASSO2(),
LASSO_plus(), and LASSO2plus(), leveraging the 'glmnet' R package with
additional steps. - Eight versatile modeling functions are offered, each
designed for predictive models across various outcomes and data types. 1)
LASSO2(), LASSO_plus(), LASSO2plus(), and LASSO2_reg() perform variable
selection using LASSO methods and construct predictive models based on
selected variables. 2) XGBtraining() employs 'XGBoost' for model building
and is the only function not involving variable selection. 3) Functions
like LASSO2_XGBtraining(), LASSOplus_XGBtraining(), and
LASSO2plus_XGBtraining() combine LASSO-related variable selection with
'XGBoost' for model construction. - All models support prediction and
validation, requiring a testing dataset comparable to the training
dataset. Additionally, the package introduces XGpred() for risk prediction
based on survival data, with the XGpred_predict() function available for
predicting risk groups in new datasets. The methodology is based on our
new algorithms and various references: - Hastie et al. (1992, ISBN 0 534
16765-9), - Therneau et al. (2000, ISBN 0-387-98784-3), - Kassambara et
al. (2021) <https://CRAN.R-project.org/package=survminer>, - Friedman et
al. (2010) <doi:10.18637/jss.v033.i01>, - Simon et al. (2011)
<doi:10.18637/jss.v039.i05>, - Harrell (2023)
<https://CRAN.R-project.org/package=rms>, - Harrell (2023)
<https://CRAN.R-project.org/package=Hmisc>, - Chen and Guestrin (2016)
<arXiv:1603.02754>, - Aoki et al. (2023) <doi:10.1200/JCO.23.01115>.

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
