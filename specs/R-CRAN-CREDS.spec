%global __brp_check_rpaths %{nil}
%global packname  CREDS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calibrated Ratio Estimator under Double Sampling Design

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Population ratio estimator (calibrated) under two-phase random sampling
design has gained enormous popularity in the recent time. This package
provides functions for estimation population ratio (calibrated) under two
phase sampling design, including the approximate variance of the ratio
estimator. The improved ratio estimator can be applicable for both the
case, when auxiliary data is available at unit level or aggregate level
(eg., mean or total) for first phase sampled. Calibration weight of each
unit of the second phase sample was calculated. Single and combined
inclusion probabilities were also estimated for both phases under two
phase random [simple random sampling without replacement (SRSWOR)]
sampling. The improved ratio estimator's percentage coefficient of
variation was also determined as a measure of accuracy. This package has
been developed based on the theoretical development of Islam et al. (2021)
and Ozgul (2020) <doi:10.1080/00949655.2020.1844702>.

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
