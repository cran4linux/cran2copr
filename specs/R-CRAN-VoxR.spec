%global __brp_check_rpaths %{nil}
%global packname  VoxR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Trees Geometry and Morphology from Unstructured TLS Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgl 
Requires:         R-grDevices 

%description
Tools for 3D point cloud voxelisation, projection, geometrical and
morphological description of trees (DBH, height, volume, crown diameter),
analyses of temporal changes between different measurement times, distance
based clustering and visualisation of 3D voxel clouds and 2D projection.
Most analyses and algorithms provided in the package are based on the
concept of space exploration and are described in Lecigne et al. (2018,
<doi:10.1093/aob/mcx095>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
