%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iNEXT.3D
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interpolation and Extrapolation for Three Dimensions of Biodiversity

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tidytree 
BuildRequires:    R-CRAN-phyclust 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tidytree 
Requires:         R-CRAN-phyclust 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-Rcpp 

%description
Biodiversity is a multifaceted concept covering different levels of
organization from genes to ecosystems. 'iNEXT.3D' extends 'iNEXT' to
include three dimensions (3D) of biodiversity, i.e., taxonomic diversity
(TD), phylogenetic diversity (PD) and functional diversity (FD). This
package provides functions to compute standardized 3D diversity estimates
with a common sample size or sample coverage. A unified framework based on
Hill numbers and their generalizations (Hill-Chao numbers) are used to
quantify 3D. All 3D estimates are in the same units of species/lineage
equivalents and can be meaningfully compared. The package features size-
and coverage-based rarefaction and extrapolation sampling curves to
facilitate rigorous comparison of 3D diversity across individual
assemblages. Asymptotic 3D diversity estimates are also provided. See Chao
et al. (2021) <doi:10.1111/2041-210X.13682> for more details.

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
