%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MTE
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Tangent Likelihood Estimation for Robust Linear Regression and Variable Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-rqPen 
Requires:         R-stats 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-rqPen 

%description
Several robust estimators for linear regression and variable selection are
provided. Included are Maximum tangent likelihood estimator by Qin, et
al., (2017), arXiv preprint <doi:10.48550/arXiv.1708.05439>, least
absolute deviance estimator and Huber regression. The penalized version of
each of these estimator incorporates L1 penalty function, i.e., LASSO and
Adaptive Lasso. They are able to produce consistent estimates for both
fixed and high-dimensional settings.

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
