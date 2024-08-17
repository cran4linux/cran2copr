%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  icosa
%global packver   0.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          Global Triangular and Penta-Hexagonal Grids Based on Tessellated Icosahedra

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-sf 

%description
Implementation of icosahedral grids in three dimensions. The
spherical-triangular tessellation can be set to create grids with custom
resolutions. Both the primary triangular and their inverted
penta-hexagonal grids can be calculated. Additional functions are provided
that allow plotting of the grids and associated data, the interaction of
the grids with other raster and vector objects, and treating the grids as
a graphs.

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
