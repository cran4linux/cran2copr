%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  betaStability
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantify the Compositional Stability of Each Community Based on a Single Sampling Event

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-elevatr 
BuildRequires:    R-CRAN-gdm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-usedist 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-elevatr 
Requires:         R-CRAN-gdm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-usedist 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-xgboost 

%description
Quantify the stability of each community based on the beta diversity
between communities gathered in a single sampling event rather than a
series of continuous sampling activities.

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
