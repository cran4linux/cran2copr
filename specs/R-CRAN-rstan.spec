%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rstan
%global packver   2.32.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.32.5
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to Stan

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       pandoc
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.1.4
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-loo >= 2.4.1
BuildRequires:    R-CRAN-StanHeaders >= 2.32.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-BH >= 1.75.0.0
BuildRequires:    R-CRAN-pkgbuild >= 1.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.9.3
BuildRequires:    R-CRAN-inline >= 0.3.19
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-QuickJSR 
Requires:         R-CRAN-RcppParallel >= 5.1.4
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-loo >= 2.4.1
Requires:         R-CRAN-StanHeaders >= 2.32.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-pkgbuild >= 1.2.0
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-inline >= 0.3.19
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-CRAN-QuickJSR 

%description
User-facing R functions are provided to parse, compile, test, estimate,
and analyze Stan models by accessing the header-only Stan library provided
by the 'StanHeaders' package. The Stan project develops a probabilistic
programming language that implements full Bayesian statistical inference
via Markov Chain Monte Carlo, rough Bayesian inference via 'variational'
approximation, and (optionally penalized) maximum likelihood estimation
via optimization. In all three cases, automatic differentiation is used to
quickly and accurately evaluate gradients without burdening the user with
the need to derive the partial derivatives.

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
