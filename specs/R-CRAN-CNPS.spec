%global __brp_check_rpaths %{nil}
%global packname  CNPS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
We unify various nonparametric hypothesis testing problems in a framework
of permutation testing, enabling hypothesis testing on multi-sample,
multidimensional data and contingency tables. Most of the functions
available in the R environment to implement permutation tests are single
functions constructed for specific test problems; to facilitate the use of
the package, the package encapsulates similar tests in a categorized
manner, greatly improving ease of use. We will all provide functions for
self-selected permutation scoring methods and self-selected p-value
calculation methods (asymptotic, exact, and sampling). For two-sample
tests, we will provide mean tests and estimate drift sizes; we will
provide tests on variance; we will provide paired-sample tests; we will
provide correlation coefficient tests under three measures. For
multi-sample problems, we will provide both ordinary and ordered
alternative test problems. For multidimensional data, we will implement
multivariate means (including ordered alternatives) and multivariate
pairwise tests based on four statistics; the components with significant
differences are also calculated. For contingency tables, we will perform
permutation chi-square test or ordered alternative.

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
