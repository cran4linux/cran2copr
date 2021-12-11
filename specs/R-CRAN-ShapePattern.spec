%global __brp_check_rpaths %{nil}
%global packname  ShapePattern
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Analyzing Shapes and Patterns

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-landscapemetrics 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-landscapemetrics 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-raster 

%description
This is an evolving and growing collection of tools for the
quantification, assessment, and comparison of shape and pattern. This
collection provides tools for: (1) the spatial decomposition of planar
shapes using 'ShrinkShape' to incrementally shrink shapes to extinction
while computing area, perimeter, and number of parts at each iteration of
shrinking; the spectra of results are returned in graphic and tabular
formats (Remmel 2015) <doi:10.1111/cag.12222>, (2) simulating landscape
patterns, (3) provision of tools for estimating composition and
configuration parameters from a categorical (binary) landscape map (grid)
and then simulates a selected number of statistically similar landscapes.
Class-focused pattern metrics are computed for each simulated map to
produce empirical distributions against which statistical comparisons can
be made. The code permits the analysis of single maps or pairs of maps
(Remmel and Fortin 2013) <doi:10.1007/s10980-013-9905-x>, (4) counting the
number of each first-order pattern element and converting that information
into both frequency and empirical probability vectors (Remmel 2020)
<doi:10.3390/e22040420>, and (5) computing the porosity of raster patches
<doi:10.3390/su10103413>. NOTE: This is a consolidation of existing
packages ('PatternClass', 'ShapePattern') to begin warehousing all shape
and pattern code in a common package. Additional utility tools for
handling data are provided and this package will be added to as more tools
are created, cleaned-up, and documented.  Note that all future
developments will appear in this package and that 'PatternClass' will
eventually be archived.

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
