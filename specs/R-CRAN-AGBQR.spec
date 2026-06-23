%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AGBQR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Generalized Bayesian Quantile Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Implements adaptive generalized Bayesian quantile regression with
quantile-specific learning rates, HAC-based calibration, Gibbs posterior
simulation, posterior summaries, predictive evaluation, and visualization
tools. The package builds on the generalized Bayesian composite quantile
regression framework of Hardy and Korobilis (2026)
<doi:10.2139/ssrn.6618603> by allowing learning rates to vary across
quantile levels. The implementation is designed for empirical work with
small and moderate time-series samples where posterior calibration and
tail-specific inference are important.

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
