%global __brp_check_rpaths %{nil}
%global packname  bayescopulareg
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Copula Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-stats 

%description
Tools for Bayesian copula generalized linear models (GLMs). The sampling
scheme is based on Pitt, Chan, and Kohn (2006)
<doi:10.1093/biomet/93.3.537>. Regression parameters (including
coefficients and dispersion parameters) are estimated via the adaptive
random walk Metropolis approach developed by Haario, Saksman, and Tamminen
(1999) <doi:10.1007/s001800050022>. The prior for the correlation matrix
is based on Hoff (2007) <doi:10.1214/07-AOAS107>.

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
