%global __brp_check_rpaths %{nil}
%global packname  npcp
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Some Nonparametric CUSUM Tests for Change-Point Detection inPossibly Multivariate Observations

License:          GPL (>= 3) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Provides nonparametric CUSUM tests for detecting changes in possibly
serially dependent univariate or multivariate observations. Retrospective
tests sensitive to changes in the expectation, the variance, the
covariance, the autocovariance, the distribution function, Spearman's rho,
Kendall's tau, Gini's mean difference, and the copula are provided, as
well as a test for detecting changes in the distribution of independent
block maxima (with environmental studies in mind). The package also
contains a test sensitive to changes in the autocopula and a combined test
of stationarity sensitive to changes in the distribution function and the
autocopula. The latest additions are a closed-end sequential test based on
empirical distribution functions that can be used for monitoring changes
in the contemporary distribution of possibly serially dependent univariate
or multivariate observations, and an open-end sequential test based on the
retrospective CUSUM statistic that can be used for monitoring changes in
the mean of possibly serially dependent univariate observations.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
