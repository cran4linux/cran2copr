%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  muse
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Unobserved Sources of Error State Space Models

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.100.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-generics >= 0.1.2
BuildRequires:    R-CRAN-greybox 
BuildRequires:    R-CRAN-smooth 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-generics >= 0.1.2
Requires:         R-CRAN-greybox 
Requires:         R-CRAN-smooth 
Requires:         R-CRAN-zoo 

%description
Implements the Power / Trend / Seasonal (PTS) model, a unified state-space
framework based on the Multiple Source of Error (MSOE) model. It brings
the trend, seasonal and irregular component models of Harvey (1989)
<doi:10.1017/CBO9781107049994>, Durbin and Koopman (2012)
<doi:10.1093/acprof:oso/9780199641178.001.0001>, Proietti (2000)
<doi:10.1016/S0169-2070(00)00037-6>, Sbrana and Silvestrini (2023)
<doi:10.1016/j.ijforecast.2022.03.003> and others together under a single
estimation, selection and forecasting interface, with an optional Box-Cox
power transformation. Models are estimated by maximum likelihood through
the Kalman filter and smoother, with automatic component selection by
information criteria.

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
