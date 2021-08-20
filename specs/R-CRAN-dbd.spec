%global __brp_check_rpaths %{nil}
%global packname  dbd
%global packver   0.0-22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.22
Release:          1%{?dist}%{?buildtag}
Summary:          Discretised Beta Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch

%description
Tools for working with a new versatile discrete distribution, the db
("discretised Beta") distribution.  This package provides density
(probability), distribution, inverse distribution (quantile) and random
data generation functions for the db family.  It provides functions to
effect conveniently maximum likelihood estimation of parameters, and a
variety of useful plotting functions.  It provides goodness of fit tests
and functions to calculate the Fisher information, different estimates of
the hessian of the log likelihood and Monte Carlo estimation of the
covariance matrix of the maximum likelihood parameter estimates.  In
addition it provides analogous tools for working with the beta-binomial
distribution which has been proposed as a competitor to the db
distribution.

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
