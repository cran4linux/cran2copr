%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  irboost
%global packver   0.1-1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Iteratively Reweighted Boosting for Robust Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mpath >= 0.4.2.21
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-mpath >= 0.4.2.21
Requires:         R-CRAN-xgboost 

%description
Fit a predictive model with the iteratively reweighted boosting (IRBoost)
that minimizes the robust loss functions in the CC-family
(concave-convex). The convex optimization is conducted by functional
descent boosting algorithm in the R package 'xgboost'. The IRBoost reduces
the weight of the observation that leads to a large loss; it also provides
weights to help identify outliers. Applications include the robust
generalized linear models and extensions, where the mean is related to the
predictors by boosting, and robust accelerated failure time models. The
package supersedes the R package 'ccboost'. Wang (2021)
<arXiv:2101.07718>.

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
