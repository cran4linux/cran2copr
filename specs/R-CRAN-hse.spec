%global packname  hse
%global packver   0.0-26
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.26
Release:          1%{?dist}%{?buildtag}
Summary:          The hse Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch

%description
Density (probability), distribution, inverse distribution (quantile) and
random data generation functions for the hse ("hope springs eternal")
distribution. Maximum likelihood estimation of parameters.  Plotting of
the probability mass function, from specified parameters or from a maximum
likelihood fit, and of the likelihood surface. Fisher information,
different estimates of the hessian of the log likelihood and Monte Carlo
estimation of the covariance matrix of the maximum likelihood parameter
estimates. Goodness of fit tests.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
