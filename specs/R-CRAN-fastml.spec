%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastml
%global packver   0.7.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.8
Release:          1%{?dist}%{?buildtag}
Summary:          Guarded Resampling Workflows for Safe and Automated Machine Learning in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-finetune 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-stats 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-finetune 
Requires:         R-CRAN-future 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-xgboost 

%description
Provides a guarded resampling workflow for training and evaluating
machine-learning models. When the guarded resampling path is used,
preprocessing and model fitting are re-estimated within each resampling
split to reduce leakage risk. Supports multiple resampling schemes,
integrates with established engines in the 'tidymodels' ecosystem, and
aims to improve evaluation reliability by coordinating preprocessing,
fitting, and evaluation within supported workflows. Offers a lightweight
AutoML-style workflow by automating model training, resampling, and tuning
across multiple algorithms, while keeping evaluation design explicit and
user-controlled.

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
