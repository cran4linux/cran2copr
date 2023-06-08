%global debug_package %{nil}
%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StanHeaders
%global packver   2.26.26
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.26.26
Release:          1%{?dist}%{?buildtag}
Summary:          C++ Header Files for Stan

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.1.4
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-RcppParallel >= 5.1.4

%description
The C++ header files of the Stan project are provided by this package, but
it contains little R code or documentation. The main reference is the
vignette. There is a shared object containing part of the 'CVODES'
library, but its functionality is not accessible from R. 'StanHeaders' is
primarily useful for developers who want to utilize the 'LinkingTo'
directive of their package's DESCRIPTION file to build on the Stan library
without incurring unnecessary dependencies. The Stan project develops a
probabilistic programming language that implements full or approximate
Bayesian statistical inference via Markov Chain Monte Carlo or
'variational' methods and implements (optionally penalized) maximum
likelihood estimation via optimization. The Stan library includes an
advanced automatic differentiation scheme, 'templated' statistical and
linear algebra functions that can handle the automatically
'differentiable' scalar types (and doubles, 'ints', etc.), and a parser
for the Stan language. The 'rstan' package provides user-facing R
functions to parse, compile, test, estimate, and analyze Stan models.

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
