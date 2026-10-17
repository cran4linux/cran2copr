%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geomorphR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Geometric Features and Footprint Comparison for 'sf' Objects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 

%description
Extracts reproducible geometric and urban-morphology descriptors from
polygon and multipart polygon building footprints stored as 'sf' objects,
including area, perimeter, compactness, shape, topology, convexity,
orientation, and optional building-height and floor-area metrics. Compares
polygon footprints across periods using the intersection-over-union
(Jaccard) index (Jaccard, 1912) <doi:10.1111/j.1469-8137.1912.tb05611.x>
to identify new constructions, potential demolitions, and footprint
changes. Supports vector file formats readable by 'sf', including
Shapefiles and GeoPackage (GPKG) vector files with named layers, optional
boundary clipping, and reprojection to a common coordinate reference
system. Returned 'sf' objects preserve source attributes and geometry for
spatial analysis and downstream workflows, with optional parallel
processing using 'future' for larger feature-extraction jobs.

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
