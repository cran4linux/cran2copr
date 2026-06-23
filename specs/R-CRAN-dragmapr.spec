%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dragmapr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Draggable Plots from Projected Geometry

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Creates interactive draggable plots from grouped projected 'sf' geometry.
The primary deliverable is a browser-based 'D3' helper where regions and
labels can be moved freely; users drag, then copy or download the
resulting offset tables. Labels can be derived automatically with
make_region_labels(), supplied directly with as_drag_labels(), and their
moved positions saved and restored with read_label_state() and
apply_label_state(). Hierarchical spatial datasets are supported via
hierarchy detection, upload profiling, make_hierarchy_key(), and
inherit_layout(), which recommend parent-child groupings and propagate
parent-level drag offsets to finer child groupings. Automatic starting
layouts are provided by suggest_offsets() using radial, grid, or
directional algorithms. Spatial file diagnostics are available through
dragmapr_diagnostics(). When a reproducible static image is also needed,
render_dragged_map() reconstructs the layout as a 'ggplot2' plot from the
source geometry plus the exported offset tables. Project bundles can be
written with write_dragmapr_project() and rendered with
render_dragmapr_project(). The interactive layer is built on the 'D3'
library: Bostock, Ogievetsky and Heer (2011) <doi:10.1109/TVCG.2011.185>.
Spatial data handling uses the 'sf' package: Pebesma (2018)
<doi:10.32614/RJ-2018-009>.

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
