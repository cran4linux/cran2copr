%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dbacf
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Autocovariance Estimation via Difference-Based Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.3
Requires:         R-core >= 2.15.3
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Matrix 

%description
Provides methods for (auto)covariance/correlation function estimation in
change point regression with stationary errors circumventing the
pre-estimation of the underlying signal of the observations. Generic,
first-order, (m+1)-gapped, difference-based autocovariance function
estimator is based on M. Levine and I. Tecuapetla-Gómez (2023)
<doi:10.48550/arXiv.1905.04578>. Bias-reducing, second-order,
(m+1)-gapped, difference-based estimator is based on I. Tecuapetla-Gómez
and A. Munk (2017) <doi:10.1111/sjos.12256>. Robust autocovariance
estimator for change point regression with autoregressive errors is based
on S. Chakar et al. (2017) <doi:10.3150/15-BEJ782>. It also includes a
general projection-based method for covariance matrix estimation.

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
