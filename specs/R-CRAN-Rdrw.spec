%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rdrw
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Univariate and Multivariate Damped Random Walk Processes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Provides tools for fitting and simulating univariate and multivariate
damped random walk processes, also known as Ornstein-Uhlenbeck processes
or first-order continuous-time autoregressive models, CAR(1) or CARMA(1,
0). The package supports irregularly spaced observation times,
heteroscedastic measurement errors, missing measurements across
multivariate time series, and polynomial mean trends in normalized time.
The current implementation models up to ten time series jointly. Kalman
filtering is used to evaluate the likelihood efficiently for maximum
likelihood estimation and Bayesian posterior sampling. Users should
preserve sufficient numerical precision when loading astronomical
observation times; see the manual for details. Also see Hu and Tak (2020)
<doi:10.48550/arXiv.2005.08049>.

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
