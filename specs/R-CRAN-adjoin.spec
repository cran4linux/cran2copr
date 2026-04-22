%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adjoin
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Constructing Adjacency Matrices Based on Spatial and Feature Similarity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-Rnanoflann 
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-Rnanoflann 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-corpcor 

%description
Constructs sparse adjacency matrices from spatial coordinates, feature
measurements, class labels, and temporal indices. Supports
nearest-neighbor graphs, heat-kernel weights, graph Laplacians, diffusion
operators, and bilateral smoothers for graph-based data analysis,
following spectral graph methods in von Luxburg (2007)
<doi:10.1007/s11222-007-9033-z>, diffusion maps in Coifman and Lafon
(2006) <doi:10.1016/j.acha.2006.04.006>, and bilateral filtering in Tomasi
and Manduchi (1998) <doi:10.1109/ICCV.1998.710815>.

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
