%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MIGEE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Impute Missing Values and Fitting Linear Mixed Effect Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-ggeffects 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-VIM 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-ggeffects 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-reshape2 

%description
Implements methods for estimating generalized estimating equations (GEE)
with advanced options for flexible modeling and handling missing data.
This package provides tools to fit and analyze GEE models for longitudinal
data, allowing users to address missingness using a variety of imputation
techniques. It supports both univariate and multivariate modeling,
visualization of missing data patterns, and facilitates the transformation
of data for efficient statistical analysis. Designed for researchers
working with complex datasets, it ensures robust estimation and inference
in longitudinal and clustered data settings.

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
