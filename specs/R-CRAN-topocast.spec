%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  topocast
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Moving-Window Regression Downscaling of Raster Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-terra >= 1.7.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-terra >= 1.7.0
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Downscales coarse-resolution raster data to a finer grid by fitting local
linear regressions of a response, such as a climate variable, on one or
more fine-resolution predictors, such as elevation and other terrain
indices, within a moving window. Regression coefficients are estimated for
every cell using summed-area tables, so the cost is independent of the
window size, then resampled to the target resolution and applied to the
fine-resolution predictors. Multiplicative and additive anomaly
application downscale time series relative to a baseline climatology,
following the regression-on-elevation approach used for high-resolution
climate surfaces described in Karger et al. (2017)
<doi:10.1038/sdata.2017.122>.

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
