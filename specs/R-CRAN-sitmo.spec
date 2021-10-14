%global __brp_check_rpaths %{nil}
%global packname  sitmo
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Pseudo Random Number Generator (PPRNG) 'sitmo' Header Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-Rcpp >= 0.12.13

%description
Provided within are two high quality and fast PPRNGs that may be used in
an 'OpenMP' parallel environment. In addition, there is a generator for
one dimensional low-discrepancy sequence. The objective of this library to
consolidate the distribution of the 'sitmo' (C++98 & C++11), 'threefry'
and 'vandercorput' (C++11-only) engines on CRAN by enabling others to link
to the header files inside of 'sitmo' instead of including a copy of each
engine within their individual package. Lastly, the package contains
example implementations using the 'sitmo' package and three accompanying
vignette that provide additional information.

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
