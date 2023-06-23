%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  landscapemetrics
%global packver   1.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.7
Release:          1%{?dist}%{?buildtag}
Summary:          Landscape Metrics for Categorical Map Patterns

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-tibble 

%description
Calculates landscape metrics for categorical landscape patterns in a tidy
workflow. 'landscapemetrics' reimplements the most common metrics from
'FRAGSTATS' (<https://www.umass.edu/landeco/>) and new ones from the
current literature on landscape metrics. This package supports 'raster'
spatial objects and takes RasterLayer, RasterStacks, RasterBricks or lists
of RasterLayer from the 'raster' package as input arguments. It further
provides utility functions to visualize patches, select metrics and
building blocks to develop new metrics.

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
