%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sae.projection
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Small Area Estimation Using Model-Assisted Projection Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidymodels 
BuildRequires:    R-CRAN-FSelector 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-bonsai 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-themis 
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-tidymodels 
Requires:         R-CRAN-FSelector 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rsample 
Requires:         R-stats 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-bonsai 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-themis 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-caret 

%description
Combines information from two independent surveys using a model-assisted
projection method. Designed for survey sampling scenarios where a large
sample collects only auxiliary information (Survey 1) and a smaller sample
provides data on both variables of interest and auxiliary variables
(Survey 2). Implements a working model to generate synthetic values of the
variable of interest by fitting the model to Survey 2 data and predicting
values for Survey 1 based on its auxiliary variables (Kim & Rao, 2012)
<doi:10.1093/biomet/asr063>.

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
