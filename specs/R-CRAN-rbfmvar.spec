%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbfmvar
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Residual-Based Fully Modified Vector Autoregression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
Implements the Residual-Based Fully Modified Vector Autoregression
(RBFM-VAR) estimator of Chang (2000) <doi:10.1017/S0266466600166071>. The
RBFM-VAR procedure extends Phillips (1995) FM-VAR to handle any unknown
mixture of I(0), I(1), and I(2) components without prior knowledge of the
number or location of unit roots. Provides automatic lag selection via
information criteria (AIC, BIC, HQ), long-run variance estimation using
Bartlett, Parzen, or Quadratic Spectral kernels with Andrews (1991)
<doi:10.2307/2938229> automatic bandwidth selection, Granger non-causality
testing with asymptotically chi-squared Wald statistics, impulse response
functions (IRF) with bootstrap confidence intervals, forecast error
variance decomposition (FEVD), and out-of-sample forecasting.

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
