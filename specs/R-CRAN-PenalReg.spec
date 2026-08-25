%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PenalReg
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Penalized Regression Analysis Using Ridge, Lasso and Elastic Net

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-caret 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides an automated framework for penalized regression analysis using
Ridge Regression, Lasso Regression and Elastic Net Regression. The package
performs data standardization, training-testing data partitioning,
cross-validation for hyperparameter tuning, model fitting, coefficient
estimation, variable importance assessment, prediction, and performance
evaluation. It simplifies regularized regression analysis by integrating
the complete modeling workflow into a single function suitable for
researchers for better understanding of the data.The methods are based on
Hoerl and Kennard (1970) <doi:10.1080/00401706.1970.10488634>, Zou and
Hastie (2005) <doi:10.1111/j.1467-9868.2005.00503.x>, and Friedman et al.
(2010) <doi:10.18637/jss.v033.i01>.

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
