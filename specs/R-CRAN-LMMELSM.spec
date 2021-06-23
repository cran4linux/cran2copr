%global __brp_check_rpaths %{nil}
%global packname  LMMELSM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Latent Multivariate Mixed Effects Location Scale Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-MASS >= 7.0
BuildRequires:    R-parallel >= 3.6.0
BuildRequires:    R-CRAN-nlme >= 3.0
BuildRequires:    R-CRAN-loo >= 2.3.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-Formula >= 1.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-MASS >= 7.0
Requires:         R-parallel >= 3.6.0
Requires:         R-CRAN-nlme >= 3.0
Requires:         R-CRAN-loo >= 2.3.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-Formula >= 1.2
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
In addition to modeling the expectation (location) of an outcome, mixed
effects location scale models (MELSMs) include submodels on the variance
components (scales) directly. This allows models on the within-group
variance with mixed effects, and between-group variances with fixed
effects. The MELSM can be used to model volatility, intraindividual
variance, uncertainty, measurement error variance, and more. Multivariate
MELSMs (MMELSMs) extend the model to include multiple correlated outcomes,
and therefore multiple locations and scales. The latent multivariate MELSM
(LMMELSM) further includes multiple correlated latent variables as
outcomes. This package implements two-level mixed effects location scale
models on multiple observed or latent outcomes, and between-group variance
modeling. Williams, Martin, Liu, and Rast (2020)
<doi:10.1027/1015-5759/a000624>. Hedeker, Mermelstein, and Demirtas (2008)
<doi:10.1111/j.1541-0420.2007.00924.x>.

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
