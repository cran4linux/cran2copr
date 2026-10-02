%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mardist
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculation of Maritime Distances

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-igraph 

%description
Tools for calculating and visualizing maritime distances and routes
between geographic points. At its core, it implements a fast Haversine
formula implemented in data.table to compute great circle distances across
sea regions (i.e. avoiding land mass). The package builds a spatial
network graph from port and cluster coordinates and uses a shortest path
algorithm to identify optimal maritime routes between origin-destination
pairs. For visualization, the package exports maps displaying individual
routes, multi-destination networks, or continuous routes through specified
waypoints. Utility functions identify the nearest network nodes to
arbitrary coordinates and handle the antimeridian discontinuities common
in Pacific maritime mapping. The package is particularly suited for
analyzing shipping lanes, trade routes, and vessel trajectory data.

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
