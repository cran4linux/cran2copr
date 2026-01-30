%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rmalschains
%global packver   0.2-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous Optimization using Memetic Algorithms with Local Search Chains (MA-LS-Chains)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.9.10
Requires:         R-CRAN-Rcpp >= 0.9.10

%description
An implementation of an algorithm family for continuous optimization
called memetic algorithms with local search chains (MA-LS-Chains), as
proposed in Molina et al. (2010) <doi:10.1162/evco.2010.18.1.18102> and
Molina et al. (2011) <doi:10.1007/s00500-010-0647-2>. Rmalschains is
further discussed in Bergmeir et al. (2016) <doi:10.18637/jss.v075.i04>.
Memetic algorithms are hybridizations of genetic algorithms with local
search methods. They are especially suited for continuous optimization.

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
