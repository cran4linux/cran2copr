%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qrcmNP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear and Penalized Quantile Regression Coefficients Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-qrcm >= 3.0
BuildRequires:    R-CRAN-survival >= 2.41
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-qrcm >= 3.0
Requires:         R-CRAN-survival >= 2.41
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Penalized and nonlinear parametric modeling of quantile regression
coefficient functions. The penalized integrated loss minimization
estimator (lasso and group lasso penalties) of Sottile, Frumento, Chiodi
and Bottai (2020) <doi:10.1177/1471082X19825523> performs covariate
selection using the information on all quantiles simultaneously. Nonlinear
parametric quantile models, in which the conditional quantile function can
be a nonlinear function of the parameters, of the covariates or both, are
estimated by integrated loss minimization as in Bottai and Cilluffo (2020)
<doi:10.1177/0962280220941159>. Both approaches extend the quantile
regression coefficients modeling framework of Frumento and Bottai (2016)
<doi:10.1111/biom.12410> implemented in 'qrcm'.

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
