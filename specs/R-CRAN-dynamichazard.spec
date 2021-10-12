%global __brp_check_rpaths %{nil}
%global packname  dynamichazard
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Hazard Models using State Space Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-survival 
Requires:         R-parallel 
Requires:         R-CRAN-boot 

%description
Contains functions that lets you fit dynamic hazard models using state
space models. The first implemented model is described in Fahrmeir (1992)
<doi:10.1080/01621459.1992.10475232> and Fahrmeir (1994)
<doi:10.1093/biomet/81.2.317>. Extensions hereof are available where the
Extended Kalman filter is replaced by an unscented Kalman filter. See
Christoffersen (2021) <doi:10.18637/jss.v099.i07> for more details.
Particle filters and smoothers are also supported more general state space
models.

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
