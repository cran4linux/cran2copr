%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PiC
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Pointcloud Interactive Computation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-conicfit 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-utils 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-conicfit 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-tictoc 
Requires:         R-utils 

%description
Provides advanced algorithms for analyzing pointcloud data from
terrestrial laser scanner in forestry applications. Key features include
fast voxelization of large datasets; segmentation of point clouds into
forest floor, understorey, canopy, and wood components. The package
enables efficient processing of large-scale forest pointcloud data,
offering insights into forest structure, connectivity, and fire risk
assessment. Algorithms to analyze pointcloud data (.xyz input file). For
more details, see Ferrara & Arrizza (2025)
<https://hdl.handle.net/20.500.14243/533471>. For single tree segmentation
details, see Ferrara et al. (2018) <doi:10.1016/j.agrformet.2018.04.008>.

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
