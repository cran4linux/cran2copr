%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geer
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bias-Reduced and Penalized Generalized Estimating Equations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-brglm2 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-brglm2 
Requires:         R-CRAN-generics 

%description
Fits marginal regression models for repeated or clustered responses using
generalized estimating equations (GEE). Provides ordinary GEE estimators,
bias-reduced and bias-corrected GEE estimators, and Jeffreys-type
penalized GEE estimators for binary, count and continuous responses.
Methods are described in Touloumis (2026a) <doi:10.48550/arXiv.2606.16043>
and Touloumis (2026b) <doi:10.48550/arXiv.2606.16058>.

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
