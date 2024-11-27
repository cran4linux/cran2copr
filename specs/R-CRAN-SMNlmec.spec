%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SMNlmec
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Scale Mixture of Normal Distribution in Linear Mixed-Effects Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.60
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-CRAN-StanHeaders >= 2.26.28
BuildRequires:    R-CRAN-rstan >= 2.26.23
BuildRequires:    R-CRAN-TruncatedNormal >= 2.2
BuildRequires:    R-CRAN-mnormt >= 2.1.1
BuildRequires:    R-CRAN-LaplacesDemon >= 16.1.6
BuildRequires:    R-CRAN-tmvtnorm >= 1.5
BuildRequires:    R-CRAN-mvtnorm >= 1.2.3
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-MASS >= 7.3.60
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-CRAN-StanHeaders >= 2.26.28
Requires:         R-CRAN-rstan >= 2.26.23
Requires:         R-CRAN-TruncatedNormal >= 2.2
Requires:         R-CRAN-mnormt >= 2.1.1
Requires:         R-CRAN-LaplacesDemon >= 16.1.6
Requires:         R-CRAN-tmvtnorm >= 1.5
Requires:         R-CRAN-mvtnorm >= 1.2.3
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-rstantools

%description
Bayesian analysis of censored linear mixed-effects models that replace
Gaussian assumptions with a flexible class of distributions, such as the
scale mixture of normal family distributions, considering a damped
exponential correlation structure which was employed to account for
within-subject autocorrelation among irregularly observed measures. For
more details, see Zhong et al. (2025, forthcoming in Statistics in
Medicine).

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
