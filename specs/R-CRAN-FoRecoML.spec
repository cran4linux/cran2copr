%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FoRecoML
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forecast Reconciliation with Machine Learning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-FoReco 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-mlr3tuning 
BuildRequires:    R-CRAN-mlr3learners 
BuildRequires:    R-CRAN-paradox 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-FoReco 
Requires:         R-stats 
Requires:         R-CRAN-cli 
Requires:         R-methods 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-mlr3tuning 
Requires:         R-CRAN-mlr3learners 
Requires:         R-CRAN-paradox 

%description
Nonlinear forecast reconciliation with machine learning in cross-sectional
(Spiliotis et al. 2021 <doi:10.1016/j.asoc.2021.107756>), temporal, and
cross-temporal (Rombouts et al. 2024
<doi:10.1016/j.ijforecast.2024.05.008>) frameworks.

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
