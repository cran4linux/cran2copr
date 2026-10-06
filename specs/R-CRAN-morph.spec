%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  morph
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          3D Segmentation of Voxels into Morphologic Classes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringr 

%description
Automatically segments a 3D array that represents a volume of binary
voxels into mutually exclusive morphological elements. This package
extends existing work for segmenting 2D binary raster data. A paper
documenting this approach has been published in the journal Landscape
Ecology: Remmel, T.K. (2022) <doi:10.1007/s10980-021-01384-7>. The output
is a cartridge (list object) that maintains the input array, the
segmentation results in array format, and a summary table. Plotting
functionality is provided to produce interactive visual outputs from the
produced results cartridge, allowing custom plotting to be performed
separately from the segmentation, which speeds-up processing. While the
old functions persist, they are being phased out and will eventually be
replaced with the new runmorph3d() and plotmorph3d() functions.

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
