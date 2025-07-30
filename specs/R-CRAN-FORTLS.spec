%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FORTLS
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Processing of Terrestrial-Based Technologies Point Cloud Data for Forestry Purposes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-Distance 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RCSF 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-VoxR 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-Distance 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-lidR 
Requires:         R-methods 
Requires:         R-CRAN-moments 
Requires:         R-parallel 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RCSF 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-VoxR 
Requires:         R-CRAN-vroom 

%description
Process automation of point cloud data derived from terrestrial-based
technologies such as Terrestrial Laser Scanner (TLS) or Mobile Laser
Scanner. 'FORTLS' enables (i) detection of trees and estimation of
tree-level attributes (e.g. diameters and heights), (ii) estimation of
stand-level variables (e.g. density, basal area, mean and dominant
height), (iii) computation of metrics related to important forest
attributes estimated in Forest Inventories at stand-level, and (iv)
optimization of plot design for combining TLS data and field measured
data. Documentation about 'FORTLS' is described in Molina-Valero et al.
(2022, <doi:10.1016/j.envsoft.2022.105337>).

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
