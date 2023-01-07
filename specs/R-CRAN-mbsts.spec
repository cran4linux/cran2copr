%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mbsts
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Bayesian Structural Time Series

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 

%description
Tools for data analysis with multivariate Bayesian structural time series
(MBSTS) models.  Specifically, the package provides facilities for
implementing general structural time series models, flexibly adding on
different time series components (trend, season, cycle, and regression),
simulating them, fitting them to multivariate correlated time series data,
conducting feature selection on the regression component.

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
