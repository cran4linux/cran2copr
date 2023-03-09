%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cosso
%global packver   2.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Regularized Nonparametric Regression Models Using COSSO Penalty

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Rglpk 
Requires:         R-parallel 
Requires:         R-CRAN-glmnet 

%description
The COSSO regularization method automatically estimates and selects
important function components by a soft-thresholding penalty in the
context of smoothing spline ANOVA models. Implemented models include mean
regression, quantile regression, logistic regression and the Cox
regression models.

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
