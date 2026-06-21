%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spacc
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Spatial Species Accumulation Curves

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-stats 
Requires:         R-parallel 

%description
High-performance spatial species accumulation curves using
nearest-neighbor algorithms. Implements 'kNN' and 'kNCN' sampling methods
with a 'C++' backend for speed. Supports Hill numbers (q=0,1,2), beta
diversity partitioning (turnover/nestedness), coverage-based rarefaction
and extrapolation, phylogenetic diversity (Faith's PD, mean pairwise
distance, mean nearest taxon distance), functional diversity accumulation,
diversity-area relationships (DAR), endemism-area curves, sampling-effort
correction and fragmentation analysis, and species-area relationship (SAR)
models based on extreme value theory (EVT). Multiple starting points
(seeds) provide uncertainty quantification. Methods are described in
'Chao' et al. (2014) <doi:10.1890/13-0133.1>, 'Baselga' (2010)
<doi:10.1111/j.1466-8238.2009.00490.x>, 'Chao' and 'Jost' (2012)
<doi:10.1890/11-1952.1>, 'Faith' (1992)
<doi:10.1016/0006-3207(92)91201-3>, 'Ma' (2018) <doi:10.1002/ece3.4526>,
'Borda-de-Agua' et al. (2025) <doi:10.1038/s41467-025-59239-7>, 'Hanski'
et al. (2013) <doi:10.1073/pnas.1311190110>, and 'Jost' (2007)
<doi:10.1890/06-1736.1>.

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
