%global __brp_check_rpaths %{nil}
%global packname  rTLS
%global packver   0.2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Process Point Clouds Derived from Terrestrial Laser Scanning

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-parallel >= 3.6.0
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-doSNOW >= 1.0.16
BuildRequires:    R-CRAN-data.table >= 1.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.870
BuildRequires:    R-CRAN-RcppProgress >= 0.4.2
BuildRequires:    R-CRAN-RcppHNSW >= 0.3.0
BuildRequires:    R-CRAN-alphashape3d 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-sp 
Requires:         R-parallel >= 3.6.0
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-doSNOW >= 1.0.16
Requires:         R-CRAN-data.table >= 1.0
Requires:         R-CRAN-RcppProgress >= 0.4.2
Requires:         R-CRAN-RcppHNSW >= 0.3.0
Requires:         R-CRAN-alphashape3d 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-sp 

%description
A set of tools to process and calculate metrics on point clouds derived
from terrestrial LiDAR (Light Detection and Ranging; TLS). Its creation is
based on key aspects of the TLS application in forestry and ecology.
Currently, the main routines are based on filtering, neighboring features
of points, voxelization, canopy structure, and the creation of artificial
stands. It is written using data.table and C++ language and in most of the
functions it is possible to use parallel processing to speed-up the
routines.

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
