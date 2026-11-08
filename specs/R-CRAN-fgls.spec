%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fgls
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Feasible GLS for Serial Correlation and Heteroskedasticity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 4.1
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-glmnet >= 4.1
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Feasible generalized least squares (FGLS) estimators for linear
regressions whose errors are serially correlated, heteroskedastic of
unknown form, or both. Serial correlation is handled by the autoregressive
filter of Perron and González-Coya (2026)
<doi:10.1016/j.jeconom.2026.106346>, estimated from a Durbin regression
whose order is chosen by an information criterion, with a variance
estimator that stays valid when the regressors are only pre-determined
rather than strictly exogenous. Heteroskedasticity is handled by the
adaptive Lasso estimate of the skedastic function of González-Coya and
Perron (2024) <doi:10.1515/jem-2023-0007>, with a bias-corrected sandwich
variance. Both corrections can be combined. Benchmark estimators (ordinary
least squares with heteroskedasticity and autocorrelation consistent
standard errors, Cochrane-Orcutt, infeasible GLS) and the simulation
designs of both papers are included.

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
