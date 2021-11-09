%global __brp_check_rpaths %{nil}
%global packname  pacotest
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Testing for Partial Copulas and the Simplifying Assumption in Vine Copulas

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-VineCopula >= 2.0.5
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-VineCopula >= 2.0.5
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 

%description
Routines for two different test types, the Constant Conditional
Correlation (CCC) test and the Vectorial Independence (VI) test are
provided (Kurz and Spanhel (2017) <arXiv:1706.02338>). The tests can be
applied to check whether a conditional copula coincides with its partial
copula. Functions to test whether a regular vine copula satisfies the
so-called simplifying assumption or to test a single copula within a
regular vine copula to be a (j-1)-th order partial copula are available.
The CCC test comes with a decision tree approach to allow testing in
high-dimensional settings.

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
