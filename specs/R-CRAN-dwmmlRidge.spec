%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dwmmlRidge
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamically Weighted Modified Maximum Likelihood (DWMML) Ridge Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Styperidge.reg 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-Styperidge.reg 

%description
Implements the dynamically weighted modified maximum likelihood ridge
(DWMMLR) regression estimator, a robust and multicollinearity-aware linear
regression estimator that combines the DWMML3 weighting procedure of Sazak
(2019) <doi:10.1080/00949655.2019.1571060> with ridge penalization to
address both outlier sensitivity and variance inflation due to
multicollinearity. The ridge parameter is selected automatically using the
approach implemented in the 'ridgregextra' package (Karadag, Sazak, and
Aydin, 2023) <https://CRAN.R-project.org/package=ridgregextra>, described
further in Karadag, Sazak, and Aydin (2026)
<doi:10.1080/02664763.2026.2655681>, which targets a variance inflation
factor (VIF) close to but not below 1, removing the need for manual
tuning. Returns comprehensive outputs (coefficients, fitted values,
residuals, mean squared error (MSE), standard errors, R-squared, and
adjusted R-squared) through a simple x/y interface.

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
