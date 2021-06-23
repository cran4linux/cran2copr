%global __brp_check_rpaths %{nil}
%global packname  rTRNG
%global packver   4.23.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.23.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced and Parallel Random Number Generation via 'TRNG'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppParallel 
Requires:         R-CRAN-Rcpp >= 0.11.6
Requires:         R-methods 
Requires:         R-CRAN-RcppParallel 

%description
Embeds sources and headers from Tina's Random Number Generator ('TRNG')
C++ library. Exposes some functionality for easier access, testing and
benchmarking into R. Provides examples of how to use parallel RNG with
'RcppParallel'. The methods and techniques behind 'TRNG' are illustrated
in the package vignettes and examples. Full documentation is available in
Bauke (2021) <https://github.com/rabauke/trng4/blob/v4.23.1/doc/trng.pdf>.

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
