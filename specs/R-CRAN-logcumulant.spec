%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  logcumulant
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Tests and Diagrams Based on Mellin Log-Cumulants

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
A family of three complementary goodness-of-fit tests based on an
adaptation of Hotelling's T-squared statistic applied to vectors of sample
log-cumulants (Mellin statistics) for positive-support reliability data.
The package provides the asymptotic chi-squared reference and parametric
bootstrap p-values for reliable finite-sample inference, covering the
Weibull, Frechet, Gamma, Inverse-Gamma, Log-Normal, and Log-Logistic
families. It also provides three diagnostic diagrams (log-cumulant,
kurtosis-skewness, and coefficient-of-variation) with bootstrap
concentration ellipses, in the spirit of moment-ratio diagrams. Methods
are described in Santos, Ospina, Espinheira and Oliveira (2025).

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
