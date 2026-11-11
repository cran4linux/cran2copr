%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  farfima
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Order Selection and Forecasting in Long-Memory Functional Time Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FCVAR 
BuildRequires:    R-CRAN-far 
BuildRequires:    R-CRAN-ftsa 
BuildRequires:    R-CRAN-longmemo 
BuildRequires:    R-CRAN-rainbow 
BuildRequires:    R-CRAN-sde 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-wwntests 
Requires:         R-CRAN-FCVAR 
Requires:         R-CRAN-far 
Requires:         R-CRAN-ftsa 
Requires:         R-CRAN-longmemo 
Requires:         R-CRAN-rainbow 
Requires:         R-CRAN-sde 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-wwntests 

%description
Provides tools for modelling, forecasting and visualising long-memory
functional time series with the functional autoregressive fractionally
integrated moving-average model. The model is fitted in three steps, each
of which can also be used on its own. First, the memory parameter is
estimated from the leading principal component scores, for example by
local Whittle or by bias-corrected local polynomial Whittle with noise.
Second, the autoregressive and moving-average orders of the fractionally
differenced curves are selected by a functional information criterion,
functional Box-Jenkins or cross-validation. Third, the operators are
estimated. The point forecasts come with conformal prediction bands that
quantify their uncertainty. Visualisation tools include improved rainbow
plots and plots of the fitted model and its forecasts.

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
