%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chopin
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Parallel Computing by Hierarchical Data Partitioning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.7.18
BuildRequires:    R-CRAN-mirai >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-sf >= 1.0.10
BuildRequires:    R-CRAN-exactextractr >= 0.8.2
BuildRequires:    R-CRAN-stars >= 0.6.0
BuildRequires:    R-CRAN-anticlust 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-collapse 
Requires:         R-CRAN-terra >= 1.7.18
Requires:         R-CRAN-mirai >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-sf >= 1.0.10
Requires:         R-CRAN-exactextractr >= 0.8.2
Requires:         R-CRAN-stars >= 0.6.0
Requires:         R-CRAN-anticlust 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-collapse 

%description
Geospatial data computation is parallelized by grid, hierarchy, or raster
files. Based on 'future' (Bengtsson, 2024
<doi:10.32614/CRAN.package.future>) and 'mirai' (Gao et al., 2025
<doi:10.32614/CRAN.package.mirai>) parallel back-ends, 'terra' (Hijmans et
al., 2025 <doi:10.32614/CRAN.package.terra>) and 'sf' (Pebesma et al.,
2024 <doi:10.32614/CRAN.package.sf>) functions as well as convenience
functions in the package can be distributed over multiple threads. The
simplest way of parallelizing generic geospatial computation is to start
from par_pad_*() functions to par_grid(), par_hierarchy(), or
par_multirasters() functions. Virtually any functions accepting classes in
'terra' or 'sf' packages can be used in the three parallelization
functions. A common raster-vector overlay operation is provided as a
function extract_at(), which uses 'exactextractr' (Baston, 2023
<doi:10.32614/CRAN.package.exactextractr>), with options for kernel
weights for summarizing raster values at vector geometries. Other
convenience functions for vector-vector operations including simple areal
interpolation (summarize_aw()) and summation of exponentially decaying
weights (summarize_sedc()) are also provided.

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
