%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiNMix
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Species N-Mixture (MNM) Models with 'nimble'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-nimble 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-rstan 
Requires:         R-stats 
Requires:         R-CRAN-abind 
Requires:         R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rstantools

%description
Simulating data and fitting multi-species N-mixture models using 'nimble'.
Includes features for handling zero-inflation and temporal correlation,
Bayesian inference, model diagnostics, parameter estimation, and
predictive checks. Designed for ecological studies with zero-altered or
time-series data. Mimnagh, N., Parnell, A., Prado, E., & Moral, R. A.
(2022) <doi:10.1007/s10651-022-00542-7>. Royle, J. A. (2004)
<doi:10.1111/j.0006-341X.2004.00142.x>.

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
