%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesRegDTR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Regression for Dynamic Treatment Regimes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.13.1
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.13.1
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-progressr 
Requires:         R-stats 
Requires:         R-CRAN-future 

%description
Methods to estimate optimal dynamic treatment regimes using Bayesian
likelihood-based regression approach as described in Yu, W., & Bondell, H.
D. (2023) <doi:10.1093/jrsssb/qkad016> Uses backward induction and dynamic
programming theory for computing expected values. Offers options for
future parallel computing.

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
