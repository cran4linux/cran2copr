%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppAnnoy
%global packver   0.0.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.21
Release:          1%{?dist}%{?buildtag}
Summary:          'Rcpp' Bindings for 'Annoy', a Library for Approximate Nearest Neighbors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
'Annoy' is a small C++ library for Approximate Nearest Neighbors written
for efficient memory usage as well an ability to load from / save to disk.
This package provides an R interface by relying on the 'Rcpp' package,
exposing the same interface as the original Python wrapper to 'Annoy'. See
<https://github.com/spotify/annoy> for more on 'Annoy'. 'Annoy' is
released under Version 2.0 of the Apache License. Also included is a small
Windows port of 'mmap' which is released under the MIT license.

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
