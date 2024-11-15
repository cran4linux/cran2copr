%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ReSurv
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Models for Predicting Claim Counts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dtplyr 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-bshazard 
BuildRequires:    R-CRAN-SynthETIC 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-SHAPforxgboost 
Requires:         R-CRAN-tidyverse 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dtplyr 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-bshazard 
Requires:         R-CRAN-SynthETIC 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-SHAPforxgboost 

%description
Prediction of claim counts using the feature based development factors
introduced in the manuscript Hiabu M., Hofman E. and Pittarello G. (2023)
<doi:10.48550/arXiv.2312.14549>. Implementation of Neural Networks,
Extreme Gradient Boosting, and Cox model with splines to optimise the
partial log-likelihood of proportional hazard models.

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
