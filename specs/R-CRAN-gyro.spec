%global __brp_check_rpaths %{nil}
%global packname  gyro
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hyperbolic Geometry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-cxhull >= 0.3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-Morpho 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-RcppCGAL 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-cxhull >= 0.3.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Rvcg 
Requires:         R-CRAN-Morpho 
Requires:         R-CRAN-purrr 
Requires:         R-grDevices 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-plotrix 
Requires:         R-graphics 
Requires:         R-CRAN-randomcoloR 

%description
Hyperbolic geometry in the hyperboloid model and the Poincaré model. The
methods are based on the gyrovector space theory developed by A. A. Ungar
that can be found in the book 'Analytic Hyperbolic Geometry: Mathematical
Foundations And Applications' <doi:10.1142/5914>. The package provides
functions to plot three-dimensional hyperbolic polyhedra, to plot
hyperbolic tilings of the Poincaré disk, and to construct and plot
Delaunay hyperbolic triangulations of the Poincaré disk. They are
constructed with the help of the C++ library 'CGAL'.

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
