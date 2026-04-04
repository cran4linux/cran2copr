%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tulpaMesh
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Delaunay Triangulation Meshes for Spatial 'SPDE' Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-RcppParallel 
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-RcppParallel 

%description
Generate constrained Delaunay triangulation meshes for use with stochastic
partial differential equation (SPDE) spatial models (Lindgren, Rue and
Lindstroem 2011 <doi:10.1111/j.1467-9868.2011.00777.x>). Provides
automatic mesh generation from point coordinates with boundary
constraints, Ruppert refinement for mesh quality, finite element method
(FEM) matrix assembly (mass, stiffness, projection), barrier models,
spherical meshes via icosahedral subdivision, and metric graph meshes for
network geometries. Built on the 'CDT' header-only C++ library (Amirkhanov
2024 <https://github.com/artem-ogre/CDT>). Designed as the mesh backend
for the 'tulpa' Bayesian hierarchical modelling engine but usable
standalone for any spatial triangulation task.

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
