%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spanner
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities to Support Lidar Applications at the Landscape, Forest, and Tree Scale

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-lidR >= 4.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-conicfit 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-cppRouting 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-lidR >= 4.2.0
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-conicfit 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-cppRouting 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-data.table 

%description
Implements algorithms for terrestrial, mobile, and airborne lidar
processing, tree detection, segmentation, and attribute estimation
(Donager et al., 2021) <doi:10.3390/rs13122297>, and a hierarchical patch
delineation algorithm 'PatchMorph' (Girvetz & Greco, 2007)
<doi:10.1007/s10980-007-9104-8>. Tree detection uses rasterized point
cloud metrics (relative neighborhood density and verticality) combined
with RANSAC cylinder fitting to locate tree boles and estimate diameter at
breast height. Tree segmentation applies graph-theory approaches inspired
by Tao et al. (2015) <doi:10.1016/j.isprsjprs.2015.08.007> with cylinder
fitting methods from de Conto et al. (2017)
<doi:10.1016/j.compag.2017.07.019>. PatchMorph delineates habitat patches
across spatial scales using organism-specific thresholds. Built on 'lidR'
(Roussel et al., 2020) <doi:10.1016/j.rse.2020.112061>.

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
