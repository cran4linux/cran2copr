%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kir
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Knowledge Integration Regression for Mean and Quantile Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-rqPen 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-rqPen 

%description
Combines observed data with prior knowledge, supplied as coefficients or
encoded from lists of important variables, for sparse mean and quantile
regression. A data-driven knowledge weight controls the contribution of
prior predictions. Knowledge Integration Quantile Regression (KIQR) uses a
Huber-smoothed quantile loss with smoothly clipped absolute deviation
(SCAD) or least absolute shrinkage and selection operator (LASSO)
penalties, as described in Wang, Lian, Yu, Zu and Zhang (2026)
<doi:10.48550/arXiv.2406.12212>. Mean regression implements the prior
LASSO of Jiang, He and Zhang (2016) <doi:10.1080/01621459.2015.1008363>
and a prior SCAD counterpart using 'ncvreg'. Provides fixed-parameter
fitting and tuning by cross-validation or a high-dimensional Bayesian
information criterion; zero-weight quantile fits use 'rqPen'.

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
