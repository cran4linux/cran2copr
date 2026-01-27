%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cycleTrendR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Cycle and Trend Analysis for Irregular Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-blocklength 
BuildRequires:    R-CRAN-fANCOVA 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lomb 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-tseries 
Requires:         R-CRAN-blocklength 
Requires:         R-CRAN-fANCOVA 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lomb 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-tseries 

%description
Provides adaptive trend estimation, cycle detection, Fourier harmonic
selection, bootstrap confidence intervals, change-point detection, and
rolling-origin forecasting. Supports LOESS (Locally Estimated Scatterplot
Smoothing), GAM (Generalized Additive Model), and GAMM (Generalized
Additive Mixed Model), and automatically handles irregular sampling using
the Lomb-Scargle periodogram. Methods implemented in this package are
described in Cleveland et al. (1990) <doi:10.2307/2289548>, Wood (2017)
<doi:10.1201/9781315370279>, and Scargle (1982) <doi:10.1086/160554>.

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
