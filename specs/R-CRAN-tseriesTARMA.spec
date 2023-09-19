%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tseriesTARMA
%global packver   0.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Nonlinear Time Series Through TARMA Models

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
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-lbfgsb3c 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-zoo 

%description
Routines for nonlinear time series analysis based on Threshold
Autoregressive Moving Average models. It provides functions and methods
for: TARMA model fitting and forecasting, tests for threshold effects,
unit-root tests based on TARMA models.

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
