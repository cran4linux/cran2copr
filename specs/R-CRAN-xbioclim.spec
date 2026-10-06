%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xbioclim
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bioclimatic Variables from Monthly Climate Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 

%description
Computes the 19 standard bioclimatic variables (BIO01-BIO19) from monthly
climate data. The variable set was originally proposed by Nix (1986,
ISBN:978-0-644-04887-3) for the BIOCLIM modelling system and is also
distributed with the CHELSA climatologies (Karger et al., 2017
<doi:10.1038/sdata.2017.122>). Provides both individual variable functions
and a unified interface to compute all 19 variables at once. Designed as
an R implementation of the 'xbioclim' C++ library (Robles Fernandez, 2026
<https://github.com/alrobles/xbioclimcpp>). Supports single-pixel vectors
and block-based raster processing via 'terra' for memory-efficient
handling of large spatial datasets. Includes helpers to transform
ERA5-Land hourly reanalysis data (Muñoz-Sabater et al., 2021
<doi:10.5194/essd-13-4349-2021>) into monthly climate inputs.

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
