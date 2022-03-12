%global __brp_check_rpaths %{nil}
%global packname  AZIAD
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Zero-Inflated and Zero-Altered Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 4.1.2
BuildRequires:    R-stats >= 4.1.2
BuildRequires:    R-base >= 4.1.2
BuildRequires:    R-methods >= 4.0.3
BuildRequires:    R-CRAN-EnvStats >= 2.6.0
BuildRequires:    R-CRAN-extraDistr >= 1.9.1
BuildRequires:    R-CRAN-rootSolve >= 1.8.2.1
BuildRequires:    R-CRAN-corpcor >= 1.6.10
BuildRequires:    R-CRAN-lqmm >= 1.5.6
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-MixAll >= 1.5.1
BuildRequires:    R-CRAN-rmutil >= 1.1.5
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-matrixcalc >= 1.0.5
BuildRequires:    R-CRAN-doParallel >= 1.0.16
BuildRequires:    R-CRAN-QRM >= 0.3.31
Requires:         R-parallel >= 4.1.2
Requires:         R-stats >= 4.1.2
Requires:         R-base >= 4.1.2
Requires:         R-methods >= 4.0.3
Requires:         R-CRAN-EnvStats >= 2.6.0
Requires:         R-CRAN-extraDistr >= 1.9.1
Requires:         R-CRAN-rootSolve >= 1.8.2.1
Requires:         R-CRAN-corpcor >= 1.6.10
Requires:         R-CRAN-lqmm >= 1.5.6
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-MixAll >= 1.5.1
Requires:         R-CRAN-rmutil >= 1.1.5
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-matrixcalc >= 1.0.5
Requires:         R-CRAN-doParallel >= 1.0.16
Requires:         R-CRAN-QRM >= 0.3.31

%description
Computes maximum likelihood estimate of general, zero inflated, and zero
altered models for discrete and continuous distributions. Computes
Kolmogorov-Smirnov (KS) test and likelihood ratio test for general,
zero-inflated, and zero-altered data. It obtains the inverse of fisher
information matrix and confidence interval for the parameters of general,
zero inflated, and zero altered models. It simulate random deviates from
zero inflated or hurdle models to obtain maximum likelihood estimate. It
is based on the work of Aldirawi et al. (2022)
<doi:10.1007/s42519-021-00230-y>.

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
