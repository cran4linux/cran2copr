%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survivalSL
%global packver   0.91
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.91
Release:          1%{?dist}%{?buildtag}
Summary:          Super Learner for Survival Prediction from Censored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-date 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-randomForestSRC 
BuildRequires:    R-CRAN-survivalmodels 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-hdnom 
BuildRequires:    R-CRAN-glmnetUtils 
BuildRequires:    R-CRAN-mosaic 
BuildRequires:    R-CRAN-mosaicCalc 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-timeROC 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-methods 
Requires:         R-splines 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-date 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-randomForestSRC 
Requires:         R-CRAN-survivalmodels 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-hdnom 
Requires:         R-CRAN-glmnetUtils 
Requires:         R-CRAN-mosaic 
Requires:         R-CRAN-mosaicCalc 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-timeROC 
Requires:         R-CRAN-rpart 
Requires:         R-methods 

%description
Several functions and S3 methods to construct a super learner in the
presence of censored times-to-event and to evaluate its prognostic
capacities.

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
