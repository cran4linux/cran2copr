%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pvarife
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Panel VAR Models with Interactive Fixed Effects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Implements the estimator of Tugan (2021) <doi:10.1093/ectj/utaa021> for
panel vector autoregression (VAR) models with interactive fixed effects.
Provides joint estimation of VAR coefficients, latent common factors, and
factor loadings via an iterative algorithm that alternates between
principal component estimation of the factors and least squares estimation
of the VAR coefficients, following the approach of Bai (2009)
<doi:10.3982/ECTA6135>. Supports impulse response functions under
recursive (Cholesky) identification, parametric confidence bands from the
joint asymptotic distribution of the estimator (Theorem 2.3), and a
classical residual bootstrap for robustness checks.

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
