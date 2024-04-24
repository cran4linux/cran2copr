%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pedbp
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pediatric Blood Pressure

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 

%description
Data and utilities for estimating pediatric blood pressure percentiles by
sex, age, and optionally height (stature) as described in Martin et.al.
(2022) <doi:10.1001/jamanetworkopen.2022.36918>. Blood pressure
percentiles for children under one year of age come from Gemelli et.al.
(1990) <doi:10.1007/BF02171556>.  Estimates of blood pressure percentiles
for children at least one year of age are informed by data from the
National Heart, Lung, and Blood Institute (NHLBI) and the Centers for
Disease Control and Prevention (CDC) <doi:10.1542/peds.2009-2107C> or from
Lo et.al. (2013) <doi:10.1542/peds.2012-1292>.  The flowchart for
selecting the informing data source comes from Martin et.al. (2022)
<doi:10.1542/hpeds.2021-005998>.

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
