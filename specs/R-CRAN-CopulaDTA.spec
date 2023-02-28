%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CopulaDTA
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Copula Based Bivariate Beta-Binomial Model for Diagnostic Test Accuracy Studies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.2.2
BuildRequires:    R-grDevices >= 4.2.2
BuildRequires:    R-CRAN-ggplot2 >= 3.4.1
BuildRequires:    R-CRAN-rstan >= 2.21.8
BuildRequires:    R-CRAN-plyr >= 1.8.8
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-stats >= 4.2.2
Requires:         R-grDevices >= 4.2.2
Requires:         R-CRAN-ggplot2 >= 3.4.1
Requires:         R-CRAN-rstan >= 2.21.8
Requires:         R-CRAN-plyr >= 1.8.8
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
Modelling of sensitivity and specificity on their natural scale using
copula based bivariate beta-binomial distribution to yield marginal mean
sensitivity and specificity. The intrinsic negative correlation between
sensitivity and specificity is modelled using a copula function. A forest
plot can be obtained for categorical covariates or for the model with
intercept only. Nyaga VN, Arbyn M, Aerts M (2017)
<doi:10.18637/jss.v082.c01>.

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
