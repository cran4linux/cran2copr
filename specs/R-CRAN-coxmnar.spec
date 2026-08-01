%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coxmnar
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cox Regression with Missing not at Random Failure Indicators

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-survival >= 3.5.0
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 

%description
Implements estimation for the Cox (1972, 1975)
<doi:10.1111/j.2517-6161.1972.tb00899.x> <doi:10.1093/biomet/62.2.269>
proportional hazards model when the failure indicator (cause of failure)
is missing not at random (MNAR), following the two adjusted
imputation-based estimating equations of Liu and Liu (2026)
<doi:10.1007/s11222-026-10857-1>. Also provided for comparison are the
full-data partial-likelihood estimator of Andersen and Gill (1982)
<doi:10.1214/aos/1176345976>, the complete-case estimator, and the
missing-at-random imputation estimator of Liu and Wang (2010, Statistica
Sinica, 20, 1125-1142). The probability models for the failure indicator
and for the missingness mechanism are estimated jointly by maximum
likelihood following Sun, Xie, and Liang (2013)
<doi:10.1007/s11425-012-4492-x>, and a Nadaraya-Watson kernel-smoothed
estimator of the missingness propensity is constructed following Qiu,
Chen, and Zhou (2015) <doi:10.1016/j.spl.2014.12.006>. Both an asymptotic
(sandwich-type) variance estimator and a nonparametric bootstrap variance
estimator are provided. When failure indicators are fully observed the
estimators reduce algebraically to the classical Cox partial-likelihood
estimator.

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
