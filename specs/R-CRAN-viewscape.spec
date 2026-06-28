%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  viewscape
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Viewscape Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-ForestTools >= 1.0.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbmcapply 
Requires:         R-CRAN-ForestTools >= 1.0.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-terra 
Requires:         R-parallel 
Requires:         R-CRAN-pbmcapply 

%description
Provides tools for viewscape analysis from one or multiple viewpoints
using a digital surface or elevation model. Core functionality includes
computing viewsheds, quantifying visual magnitude, calculating a suite of
viewscape configuration metrics (extent, depth, relief, Sky View Factor,
skyline variation, and patch-based landscape structure), Shannon Diversity
Index and land cover feature proportions within the visible area, pairwise
intervisibility networks, panoramic view generation, and visualizing
results as rasters or polygons. Viewscape configuration metrics follow the
methods of Tabrizian et al. (2020)
<doi:10.1016/j.landurbplan.2019.103704>. The viewshed algorithm is based
on Franklin & Ray (1994)
<https://api.semanticscholar.org/CorpusID:10680920> and Wang et al. (2000)
<https://api.semanticscholar.org/CorpusID:131687018>. Visual magnitude is
derived from Chamberlain & Meitner (2013)
<doi:10.1016/j.landurbplan.2013.01.003>. Sky View Factor is computed
following Oke (1981) <doi:10.1002/joc.3370010304> as implemented in the
'shadow' package (Dorman et al. 2019) <doi:10.32614/RJ-2019-024>.

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
