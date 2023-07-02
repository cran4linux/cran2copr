%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gyro
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hyperbolic Geometry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-cxhull >= 0.3.0
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Morpho 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-RCDT 
BuildRequires:    R-CRAN-randomcoloR 
Requires:         R-CRAN-cxhull >= 0.3.0
Requires:         R-CRAN-clipr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Morpho 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-Rvcg 
Requires:         R-CRAN-RCDT 
Requires:         R-CRAN-randomcoloR 

%description
Hyperbolic geometry in the Minkowski model and the Poincaré model. The
methods are based on the gyrovector space theory developed by A. A. Ungar
that can be found in the book 'Analytic Hyperbolic Geometry: Mathematical
Foundations And Applications' <doi:10.1142/5914>. The package provides
functions to plot three-dimensional hyperbolic polyhedra and to plot
hyperbolic tilings of the Poincaré disk.

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
