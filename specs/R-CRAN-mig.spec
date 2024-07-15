%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mig
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Inverse Gaussian Distribution

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-TruncatedNormal >= 2.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-TruncatedNormal >= 2.3
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-statmod 

%description
Provides utilities for estimation for the multivariate inverse Gaussian
distribution of Minami (2003) <doi:10.1081/STA-120025379>, including
random vector generation and explicit estimators of the location vector
and scale matrix. The package implements kernel density estimators
discussed in Belzile, Desgagnes, Genest and Ouimet (2024)
<doi:10.48550/arXiv.2209.04757> for smoothing multivariate data on
half-spaces.

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
