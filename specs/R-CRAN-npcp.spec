%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npcp
%global packver   0.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Some Nonparametric CUSUM Tests for Change-Point Detection in Possibly Multivariate Observations

License:          GPL (>= 3) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-sandwich 

%description
Provides nonparametric CUSUM tests for detecting changes in possibly
serially dependent univariate or low-dimensional multivariate
observations. Retrospective tests sensitive to changes in the expectation,
the variance, the covariance, the autocovariance, the distribution
function, Spearman's rho, Kendall's tau, Gini's mean difference, and the
copula are provided, as well as a test for detecting changes in the
distribution of independent block maxima (with environmental studies in
mind). The package also contains a test sensitive to changes in the
autocopula and a combined test of stationarity sensitive to changes in the
distribution function and the autocopula. The latest additions are an
open-end sequential test based on the retrospective CUSUM statistic that
can be used for monitoring changes in the mean of possibly serially
dependent univariate observations, as well as closed-end and open-end
sequential tests based on empirical distribution functions that can be
used for monitoring changes in the contemporary distribution of possibly
serially dependent univariate or low-dimensional multivariate
observations.

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
