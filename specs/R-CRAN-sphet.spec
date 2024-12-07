%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sphet
%global packver   2.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Spatial Autoregressive Models with and without Heteroskedastic Innovations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-spData >= 2.3.1
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-spatialreg 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-spData >= 2.3.1
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-spatialreg 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-sf 

%description
Functions for fitting Cliff-Ord-type spatial autoregressive models with
and without heteroskedastic innovations using Generalized Method of
Moments estimation are provided. Some support is available for fitting
spatial HAC models, and for fitting with non-spatial endogeneous variables
using instrumental variables.

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
