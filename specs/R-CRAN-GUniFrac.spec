%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GUniFrac
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized UniFrac Distances, Distance-Based Multivariate Methods and Feature-Based Univariate Methods for Microbiome Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-rmutil 
BuildRequires:    R-CRAN-dirmult 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-modeest 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ape 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-rmutil 
Requires:         R-CRAN-dirmult 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-modeest 
Requires:         R-CRAN-inline 
Requires:         R-methods 

%description
A suite of methods for powerful and robust microbiome data analysis
including data normalization, data simulation, community-level association
testing and differential abundance analysis. It implements generalized
UniFrac distances, Geometric Mean of Pairwise Ratios (GMPR) normalization,
semiparametric data simulator, distance-based statistical methods, and
feature-based statistical methods. The distance-based statistical methods
include three extensions of PERMANOVA: (1) PERMANOVA using the
Freedman-Lane permutation scheme, (2) PERMANOVA omnibus test using
multiple matrices, and (3) analytical approach to approximating PERMANOVA
p-value. Feature-based statistical methods include linear model-based
methods for differential abundance analysis of zero-inflated
high-dimensional compositional data.

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
