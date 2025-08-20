%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ETASbootstrap
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap Confidence Interval Estimation for 'ETAS' Model Parameters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.58.2
BuildRequires:    R-stats >= 4.2.2
BuildRequires:    R-utils >= 4.2.2
BuildRequires:    R-CRAN-spatstat.geom >= 3.2.8
BuildRequires:    R-CRAN-ETAS >= 0.5.1
Requires:         R-CRAN-MASS >= 7.3.58.2
Requires:         R-stats >= 4.2.2
Requires:         R-utils >= 4.2.2
Requires:         R-CRAN-spatstat.geom >= 3.2.8
Requires:         R-CRAN-ETAS >= 0.5.1

%description
The 2-D spatial and temporal Epidemic Type Aftershock Sequence ('ETAS')
Model is widely used to 'decluster' earthquake data catalogs. Usually, the
calculation of standard errors of the 'ETAS' model parameter estimates is
based on the Hessian matrix derived from the log-likelihood function of
the fitted model. However, when an 'ETAS' model is fitted to a local data
set over a time period that is limited or short, the standard errors based
on the Hessian matrix may be inaccurate. It follows that the asymptotic
confidence intervals for parameters may not always be reliable. As an
alternative, this package allows for the construction of bootstrap
confidence intervals based on empirical quantiles for the parameters of
the 2-D spatial and temporal 'ETAS' model. This version improves on
Version 0.1.0 of the package by enabling the study space window (renamed
'study region') to be polygonal rather than merely rectangular. A Japan
earthquake data catalog is used in a second example to illustrate this new
feature.

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
