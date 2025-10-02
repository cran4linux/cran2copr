%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  degradr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Remaining Useful Life with Linear Mixed Effects Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5
Requires:         R-core >= 4.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-ggplot2 

%description
Provides tools for estimating the Remaining Useful Life (RUL) of degrading
systems using linear mixed-effects models and creating a health index. It
supports both univariate and multivariate degradation signals. For
multivariate inputs, the signals are merged into a univariate health index
prior to modeling. Linear and exponential degradation trajectories are
supported (the latter using a log transformation). Remaining Useful Life
(RUL) distributions are estimated using Bayesian updating for new units,
enabling on-site predictive maintenance. Based on the methodology of Liu
and Huang (2016) <doi:10.1109/TASE.2014.2349733>.

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
