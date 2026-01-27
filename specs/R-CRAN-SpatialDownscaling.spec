%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpatialDownscaling
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Spatial Downscaling Using Deep Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-keras3 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-abind 
Requires:         R-stats 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-keras3 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-abind 

%description
The aim of the spatial downscaling is to increase the spatial resolution
of the gridded geospatial input data. This package contains two deep
learning based spatial downscaling methods, super-resolution deep residual
network (SRDRN) (Wang et al., 2021 <doi:10.1029/2020WR029308>) and UNet
(Ronneberger et al., 2015 <doi:10.1007/978-3-319-24574-4_28>), along with
a statistical baseline method bias correction and spatial disaggregation
(Wood et al., 2004 <doi:10.1023/B:CLIM.0000013685.99609.9e>). The SRDRN
and UNet methods are implemented to optionally account for cyclical
temporal patterns in case of spatio-temporal data. For more details of the
methods, see Sipilä et al. (2025) <doi:10.48550/arXiv.2512.13753>.

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
