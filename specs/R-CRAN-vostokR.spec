%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vostokR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Solar Potential Calculation for Point Clouds using 'VOSTOK'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-lidR >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-lidR >= 4.0.0
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-terra 
Requires:         R-methods 

%description
Calculate solar potential for LiDAR point clouds using the 'VOSTOK' (Voxel
Octree Solar Toolkit) algorithm. This R program provides an interface to
the original 'VOSTOK' C++ implementation by Bechtold and Hofle (2020),
enabling efficient ray casting and solar position algorithms to compute
solar irradiance for each point while accounting for shadowing effects.
Integrates seamlessly with the 'lidR' package for LiDAR data processing
workflows. The original 'VOSTOK' toolkit is available at
<doi:10.11588/data/QNA02B>.

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
