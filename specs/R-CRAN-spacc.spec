%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spacc
%global packver   0.11.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.0
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
High-performance spatial species accumulation curves using fixed-focus
spatially constrained rarefaction, nearest-centroid expansion, and
nearest-neighbor walks with a C++ backend for speed. Supports Hill numbers
(q=0,1,2), beta diversity partitioning (turnover/nestedness) at site and
pooled resolution, coverage-based rarefaction and extrapolation of alpha
and beta diversity, phylogenetic diversity (PD; Faith's PD, EvoHeritage,
mean pairwise distance, mean nearest taxon distance), functional diversity
accumulation including aggregated functional diversity and intraspecific
trait variation, phylogenetic and functional redundancy, interaction
network accumulation, diversity-area relationships (DAR), endemism-area
curves, sampling-effort correction and fragmentation analysis,
species-area relationship (SAR) models based on extreme value theory
(EVT), and area-based richness extrapolation via the total-species curve.
Total richness is also estimated from frequency counts, including the
accumulation rate curve estimator and an estimator for sites sampled
without replacement, and shift-and-rotate null models test the position of
a sampling design. Multiple starting points (seeds) provide uncertainty
quantification. Methods are described in Chao et al. (2014)
<doi:10.1890/13-0133.1>, Baselga (2010)
<doi:10.1111/j.1466-8238.2009.00490.x>, Chao and Jost (2012)
<doi:10.1890/11-1952.1>, Faith (1992) <doi:10.1016/0006-3207(92)91201-3>,
Ma (2018) <doi:10.1002/ece3.4425>, Borda-de-Agua et al. (2025)
<doi:10.1038/s41467-025-59239-7>, Hanski et al. (2013)
<doi:10.1073/pnas.1311190110>, Jost (2007) <doi:10.1890/06-1736.1>, Ugland
et al. (2003) <doi:10.1046/j.1365-2656.2003.00748.x>, Chao et al. (2023)
<doi:10.1002/ecm.1588>, Chiu (2023) <doi:10.1111/2041-210X.14146>, Chiu et
al. (2023) <doi:10.1098/rstb.2022.0183>, Rosindell et al. (2024)
<doi:10.1093/sysbio/syad072>, Wojcik et al. (2024)
<doi:10.1111/2041-210X.14470>, Ridder et al. (2024)
<doi:10.1111/2041-210X.14443>, Jones et al. (2025)
<doi:10.1111/ddi.70080>, and Shestopaloff (2025)
<doi:10.1007/s10651-025-00644-y>.

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
