%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDSpatialScan
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate and Functional Spatial Scan Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-SpatialNP 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-CRAN-swfscMisc 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-SpatialNP 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-fmsb 
Requires:         R-CRAN-swfscMisc 
Requires:         R-CRAN-raster 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Allows to detect spatial clusters of abnormal values on multivariate or
functional data (Frévent et al. (2022) <doi:10.32614/RJ-2022-045>). See
also: Frévent et al. (2023) <doi:10.1093/jrsssc/qlad017>, Smida et al.
(2022) <doi:10.1016/j.csda.2021.107378>, Frévent et al. (2021)
<doi:10.1016/j.spasta.2021.100550>. Cucala et al. (2019)
<doi:10.1016/j.spasta.2018.10.002>, Cucala et al. (2017)
<doi:10.1016/j.spasta.2017.06.001>, Jung and Cho (2015)
<doi:10.1186/s12942-015-0024-6>, Kulldorff et al. (2009)
<doi:10.1186/1476-072X-8-58>.

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
