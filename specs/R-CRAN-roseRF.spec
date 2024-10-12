%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  roseRF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          ROSE Random Forests for Robust Semiparametric Efficient Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.93
BuildRequires:    R-CRAN-glmnet >= 4.1.6
BuildRequires:    R-CRAN-mlr >= 2.19.1
BuildRequires:    R-CRAN-tuneRanger >= 0.5
BuildRequires:    R-CRAN-ranger >= 0.14.1
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-ParamHelpers 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-caret >= 6.0.93
Requires:         R-CRAN-glmnet >= 4.1.6
Requires:         R-CRAN-mlr >= 2.19.1
Requires:         R-CRAN-tuneRanger >= 0.5
Requires:         R-CRAN-ranger >= 0.14.1
Requires:         R-CRAN-keras 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-ParamHelpers 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-rpart 
Requires:         R-stats 
Requires:         R-CRAN-xgboost 

%description
ROSE (RObust Semiparametric Efficient) random forests for robust
semiparametric efficient estimation in partially parametric models
(containing generalised partially linear models). Details can be found in
the paper by Young and Shah (2024) <doi:10.48550/arXiv.2410.03471>.

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
