%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tseriesTARMA
%global packver   0.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Nonlinear Time Series Through Threshold Autoregressive Moving Average Models (TARMA) Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-lbfgsb3c 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-fitdistrplus 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-lbfgsb3c 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-fitdistrplus 

%description
Routines for nonlinear time series analysis based on Threshold
Autoregressive Moving Average (TARMA) models. It provides functions and
methods for: TARMA model fitting and forecasting, including robust
estimators, see Goracci et al. JBES (2025)
<doi:10.1080/07350015.2024.2412011>; tests for threshold effects, see
Giannerini et al. JoE (2024) <doi:10.1016/j.jeconom.2023.01.004>, Goracci
et al. Statistica Sinica (2023) <doi:10.5705/ss.202021.0120>, Angelini et
al. (2024) <doi:10.48550/arXiv.2308.00444>; unit-root tests based on TARMA
models, see Chan et al. Statistica Sinica (2024)
<doi:10.5705/ss.202022.0125>.

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
