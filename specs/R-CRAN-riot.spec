%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  riot
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Inputs/Outputs for Tractography

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rvtk >= 0.2.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fiber 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-rvtk >= 0.2.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fiber 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 

%description
Provides a unified input-output interface for reading and writing bundles
— collections of 3-D polylines (streamlines) reconstructed by
fibre-tracking algorithms applied to diffusion MRI data. Supported formats
include VTK (.vtk), VTP (.vtp), medInria FDS (.fds), MRtrix TCK/TSF
(.tck/.tsf), and TrackVis TRK (.trk), with additional formats accessible
via the 'DIPY' Python library through 'reticulate'. Bundles are
represented in R using the S7 classes defined in the 'fiber' package: a
single tract (class 'streamline') stores its coordinates, per-point scalar
attributes, and per-streamline scalar attributes in separate, typed slots;
a collection of tracts (class 'bundle') wraps a list of streamlines
together with optional bundle-level metadata. VTK support is provided at
compile time by the 'rvtk' package, which supplies pre-compiled VTK
libraries and headers so that no manual VTK installation is required on
most platforms.

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
