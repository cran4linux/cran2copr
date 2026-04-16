%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  betaARMA
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Beta Autoregressive Moving Average Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
Requires:         R-CRAN-forecast 

%description
Fits Beta Autoregressive Moving Average (BARMA) models for time series
data distributed in the standard unit interval (0, 1). The estimation is
performed via the conditional maximum likelihood method using the
Broyden-Fletcher-Goldfarb-Shanno (BFGS) quasi-Newton algorithm. The
package includes tools for model fitting, diagnostic checking, and
forecasting. Based on the work of Rocha and Cribari-Neto (2009)
<doi:10.1007/s11749-008-0112-z> and the associated erratum Rocha and
Cribari-Neto (2017) <doi:10.1007/s11749-017-0528-4>. The original code was
developed by Fabio M. Bayer.

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
