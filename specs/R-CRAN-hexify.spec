%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hexify
%global packver   0.3.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.10
Release:          1%{?dist}%{?buildtag}
Summary:          Equal-Area Hex Grids on the 'Snyder' 'ISEA' 'Icosahedron'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-rlang 

%description
Provides functions to build and use equal-area hexagonal discrete global
grids using the 'Snyder' 'ISEA' projection ('Snyder' 1992
<doi:10.3138/27H7-8K88-4882-1752>). Implements the 'ISEA' discrete global
grid system ('Sahr', 'White' and 'Kimerling' 2003
<doi:10.1559/152304003100011090>). Includes a fast 'C++' core for
projection and aperture quantization, and 'sf'/'terra'-compatible R
wrappers for grid generation and coordinate assignment. Output is
compatible with 'dggridR' for interoperability.

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
