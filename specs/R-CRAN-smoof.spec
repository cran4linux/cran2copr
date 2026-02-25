%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smoof
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Single and Multi-Objective Optimization Test Functions

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-ParamHelpers >= 1.8
BuildRequires:    R-CRAN-BBmisc >= 1.6
BuildRequires:    R-CRAN-checkmate >= 1.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-ParamHelpers >= 1.8
Requires:         R-CRAN-BBmisc >= 1.6
Requires:         R-CRAN-checkmate >= 1.1
Requires:         R-CRAN-Rcpp >= 0.11.0

%description
Provides generators for a high number of both single- and multi- objective
test functions which are frequently used for the benchmarking of
(numerical) optimization algorithms. Moreover, it offers a set of
convenient functions to generate, plot and work with objective functions.

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
