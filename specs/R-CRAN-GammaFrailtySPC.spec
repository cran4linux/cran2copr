%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GammaFrailtySPC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Process Control Based on Gamma-Frailty AFT Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Implements statistical process control ('SPC') monitoring schemes for
heterogeneous reliability observations using Accelerated Failure Time
('AFT') models integrated with continuous gamma frailty. It accommodates
both uncensored and right-censored reliability observations in the
presence of observed and unobserved covariates. Provides Phase I maximum
likelihood estimation of Weibull 'AFT' gamma frailty model parameters, and
Phase II monitoring procedures including probability-limits-based control
charts, exponentially weighted moving average ('EWMA') charts with
conditional expected values, and likelihood-ratio cumulative sum ('CUSUM')
control charts. Competing 'CUSUM' schemes (ignoring unobserved frailty or
both covariates) and Average Run Length ('ARL') simulation utilities are
also provided. The statistical methodology is based on Asadzadeh (2022)
<doi:10.1080/00949655.2021.1959582>.

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
