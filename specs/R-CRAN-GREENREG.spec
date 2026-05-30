%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GREENREG
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tool for Statistical and Environmental Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lmtest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-stats 
Requires:         R-CRAN-lmtest 

%description
Provides a set of accessible and automated functions to apply statistical
models such as Simple Linear Regression (RLS, from the Spanish 'Regresión
Lineal Simple'), Multiple Linear Regression (RLM, from the Spanish
'Regresión Lineal Múltiple'), Generalized Linear Models (GLM), and time
series analysis through Autoregressive Integrated Moving Average (ARIMA)
models. Designed to support teaching at the Universidad Autónoma Chapingo,
it facilitates results interpretation and assumption validation through
automatic graphical diagnostics. Methods for regression and time series
are based on Montgomery et al. (2021, ISBN:978-1119570141) and Box &
Jenkins (1970, ISBN:978-0816211043).

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
