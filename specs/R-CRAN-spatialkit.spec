%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatialkit
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Tessellation, Modeling, and Cross-Validation Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-sf >= 1.0
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-logger 
Requires:         R-CRAN-digest 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-parallel 

%description
Constructs analysis regions from the distribution of the data itself, as
an alternative to aggregating onto administrative boundaries that were
drawn for unrelated purposes. Seeds and builds Voronoi, Delaunay,
hexagonal and square tessellations with reproducible identifiers, selects
a cell count from the spatial structure of the observations, assigns
features to cells, and aggregates to cell level with optional
design-effect corrections so that standard errors account for within-cell
autocorrelation. Also manages coordinate reference systems. Fits
geographically weighted regression (via 'GWmodel'; Lu et al. (2014)
<doi:10.1080/10095020.2014.917453>), Bayesian spatial Gaussian process
regression (via 'brms', using the Hilbert space approximation of
Riutort-Mayol et al. (2023) <doi:10.1007/s11222-022-10167-2>) and random
forests (via 'ranger', with the permutation importance of Strobl et al.
(2007) <doi:10.1186/1471-2105-8-25>), each behind one S3 class with
consistent predict, fitted, residuals and plot methods. Provides spatial
cross-validation with random, block, buffered, leave-location-out and
nearest-neighbour distance-matched folds (Mila et al. (2022)
<doi:10.1111/2041-210X.13851>), forward variable selection, model
comparison, prediction onto a regular surface, and the area of
applicability of Meyer and Pebesma (2021) <doi:10.1111/2041-210X.13650> to
flag where a fitted model extrapolates beyond its training data.

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
