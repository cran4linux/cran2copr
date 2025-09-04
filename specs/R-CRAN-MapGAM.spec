%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MapGAM
%global packver   1.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mapping Smoothed Effect Estimates from Individual-Level Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-PBSmapping 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-PBSmapping 

%description
Contains functions for mapping odds ratios, hazard ratios, or other effect
estimates using individual-level data such as case-control study data,
using generalized additive models (GAMs) or Cox models for smoothing with
a two-dimensional predictor (e.g., geolocation or exposure to chemical
mixtures) while adjusting linearly for confounding variables, using
methods described by Kelsall and Diggle (1998), Webster at al. (2006), and
Bai et al. (2020).  Includes convenient functions for mapping point
estimates and confidence intervals, efficient control sampling, and
permutation tests for the null hypothesis that the two-dimensional
predictor is not associated with the outcome variable (adjusting for
confounders).

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
