%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MeshesOperations
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Operations on 3D Meshes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
BuildRequires:    mpfr-devel
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-RcppCGAL 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Rvcg 

%description
Uses the 'CGAL' C++ library to perform operations on 3D meshes: Boolean
operations (intersection, union, difference), Minkowski sum, smoothing,
clipping, decomposition into convex parts.

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
