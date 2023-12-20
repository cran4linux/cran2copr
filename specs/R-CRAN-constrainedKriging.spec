%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  constrainedKriging
%global packver   0.2-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained, Covariance-Matching Constrained and Universal Point or Block Kriging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9
Requires:         R-core >= 2.9
BuildRequires:    R-CRAN-sf >= 1.0.14
BuildRequires:    R-CRAN-sp >= 0.9.60
BuildRequires:    R-CRAN-spatialCovariance >= 0.6.4
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-sf >= 1.0.14
Requires:         R-CRAN-sp >= 0.9.60
Requires:         R-CRAN-spatialCovariance >= 0.6.4
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 

%description
Provides functions for efficient computation of non-linear spatial
predictions with local change of support (Hofer, C. and Papritz, A. (2011)
"constrainedKriging: An R-package for customary, constrained and
covariance-matching constrained point or block kriging"
<doi:10.1016/j.cageo.2011.02.009>).  This package supplies functions for
two-dimensional spatial interpolation by constrained (Cressie, N. (1993)
"Aggregation in geostatistical problems"
<doi:10.1007/978-94-011-1739-5_3>), covariance-matching constrained
(Aldworth, J. and Cressie, N. (2003) "Prediction of nonlinear spatial
functionals" <doi:10.1016/S0378-3758(02)00321-X>) and universal (external
drift) Kriging for points or blocks of any shape from data with a
non-stationary mean function and an isotropic weakly stationary covariance
function.  The linear spatial interpolation methods, constrained and
covariance-matching constrained Kriging, provide approximately unbiased
prediction for non-linear target values under change of support.  This
package extends the range of tools for spatial predictions available in R
and provides an alternative to conditional simulation for non-linear
spatial prediction problems with local change of support.

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
