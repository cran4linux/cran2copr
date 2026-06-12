%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MacroFilters
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Trend-Cycle Decomposition for Macroeconomic Time Series

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-tseries 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-tseries 

%description
Provides high-performance tools for macroeconomic trend extraction and
filtering, specifically designed to solve the end-point problem in
real-time. Implements the MacroBoost Hybrid (MBH) filter using penalized
P-splines and gradient boosting. Unlike the standard Hodrick-Prescott
filter, 'MacroFilters' utilizes component-wise L2-boosting with robust
loss functions (Huber) to handle extreme transient shocks (e.g., COVID-19)
without inducing spurious trend shifts. The algorithm includes an
automated two-layer diagnostic stage for unit roots and structural breaks,
optimized via corrected AICc for computational efficiency. Methodology
detailed in Kinel (2026) <doi:10.2139/ssrn.6371138>.

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
