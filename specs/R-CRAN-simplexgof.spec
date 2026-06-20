%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simplexgof
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap-Calibrated Goodness-of-Fit Test for Simplex Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Implements the bootstrap-calibrated local-influence goodness-of-fit test
for simplex regression models with constant or varying dispersion,
following the local influence approach of Zhu and Zhang (2004)
<doi:10.1093/biomet/91.3.579> and the simplex regression model of
Barndorff-Nielsen and Jorgensen (1991) <doi:10.1016/0047-259X(91)90008-P>.
The test statistic aggregates individual local-influence measures under
case-weight perturbation. Because the first-order asymptotic normal
calibration is severely liberal in finite samples, a parametric bootstrap
calibration is provided that restores accurate size control and delivers
high power against omitted covariates, neglected dispersion, and
distributional misspecification. Plotting functions reproduce the figures
and tables of the companion methodological paper. Computational kernels
are implemented in 'C++' via 'Rcpp' and 'RcppArmadillo' for speed, and two
real datasets are bundled.

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
