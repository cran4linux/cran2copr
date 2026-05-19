%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sobol
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quasi-Monte Carlo Sobol Sequence Generator

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-methods 
Requires:         R-CRAN-checkmate 

%description
Provides a fast and efficient implementation of Sobol sequences for
quasi-Monte Carlo methods. The Sobol sequence is a low-discrepancy
sequence with the property that for all values of N, its subsequence x1,
..., xN has a low discrepancy. It can be used to generate quasi-random
numbers for use in Monte Carlo integration and other simulation methods.
This implementation is based on the algorithms described by Bratley and
Fox (1988) <doi:10.1145/42288.214372> and uses direction numbers from Joe
and Kuo (2008) <doi:10.1145/1358628.1358630>. The package includes both
batch and incremental interfaces with support for arbitrary starting
indices and reproducible sequences. It uses 'Rcpp' for efficient 'C++'
integration.

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
