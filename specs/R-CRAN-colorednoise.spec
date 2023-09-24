%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  colorednoise
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Temporally Autocorrelated Populations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats >= 3.3.2
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-purrr >= 0.2.3

%description
Temporally autocorrelated populations are correlated in their vital rates
(growth, death, etc.) from year to year. It is very common for
populations, whether they be bacteria, plants, or humans, to be temporally
autocorrelated. This poses a challenge for stochastic population modeling,
because a temporally correlated population will behave differently from an
uncorrelated one. This package provides tools for simulating populations
with white noise (no temporal autocorrelation), red noise (positive
temporal autocorrelation), and blue noise (negative temporal
autocorrelation).  The algebraic formulation for autocorrelated noise
comes from Ruokolainen et al. (2009) <doi:10.1016/j.tree.2009.04.009>.
Models for unstructured populations and for structured populations (matrix
models) are available.

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
