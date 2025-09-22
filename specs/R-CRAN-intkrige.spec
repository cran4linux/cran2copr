%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  intkrige
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Numerical Implementation of Interval-Valued Kriging

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
An interval-valued extension of ordinary and simple kriging. Optimization
of the function is based on a generalized interval distance. This creates
a non-differentiable cost function that requires a differentiable
approximation to the absolute value function. This differentiable
approximation is optimized using a Newton-Raphson algorithm with a penalty
function to impose the constraints. Analyses in the package are driven by
the 'intsp' and 'intgrd' classes, which are interval-valued extensions of
'SpatialPointsDataFrame' and 'SpatialPixelsDataFrame' respectively. The
package includes several wrappers to functions in the 'gstat' and 'sp'
packages.

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
