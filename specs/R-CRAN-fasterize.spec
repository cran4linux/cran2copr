%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fasterize
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Polygon to Raster Conversion

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-raster >= 2.8.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-wk 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-raster >= 2.8.3
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-wk 

%description
Provides a drop-in replacement for rasterize() from the 'raster' package
that takes polygon vector or data frame objects, and is much faster. There
is support for the main options provided by the rasterize() function,
including setting the field used and background value, and options for
aggregating multi-layer rasters. Uses the scan line algorithm attributed
to Wylie et al. (1967) <doi:10.1145/1465611.1465619>.

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
