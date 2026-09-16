%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  T1FF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Type-1 Fuzzy Functions for Classification, Regression, and Forecasting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-kernlab 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits Type-1 Fuzzy Function models for binary classification, numeric
regression, and time-series forecasting with user-supplied temporal
predictors. The package combines fuzzy C-means memberships, nonlinear
membership transformations, cluster-specific linear or support vector
machine models, and membership-weighted predictions. It also provides
model evaluation, validation, K-fold and stratified K-fold tuning, and
repeated nested cross-validation with task-appropriate metrics. The
regression workflow can be used for forecasting when temporal dependence
is represented by lagged or seasonal predictors and assessment partitions
preserve chronological order.

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
