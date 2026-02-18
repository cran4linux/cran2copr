%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CspStandSegmentation
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comparative Shortest Path Forest Stand Segmentation from LiDAR Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-RCSF 
BuildRequires:    R-CRAN-conicfit 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-lidR 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-RCSF 
Requires:         R-CRAN-conicfit 
Requires:         R-CRAN-rgl 

%description
Functionality for segmenting individual trees from a forest stand scanned
with a close-range (e.g., terrestrial or mobile) laser scanner. The
complete workflow from a raw point cloud to a complete tabular forest
inventory is provided. The package contains several algorithms for
detecting tree bases and a graph-based algorithm to attach all remaining
points to these tree bases. It builds heavily on the 'lidR' package. A
description of the segmentation algorithm can be found in Larysch et al.
(2025) <doi:10.1007/s10342-025-01796-z>.

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
