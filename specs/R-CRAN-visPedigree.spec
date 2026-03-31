%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visPedigree
%global packver   1.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tidying, Analysis, and Fast Visualization of Animal and Plant Pedigrees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-igraph >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-igraph >= 1.3.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lattice 

%description
Provides tools for the analysis and visualization of animal and plant
pedigrees. Analytical methods include equivalent complete generations,
generation intervals, effective population size (via inbreeding,
coancestry, and demographic approaches), founder and ancestor
contributions, partial inbreeding, genetic diversity indices, and additive
(A), dominance (D), and epistatic (AA) relationship matrices. Core
algorithms — ancestry tracing, topological sorting, inbreeding
coefficients, and matrix construction — are implemented in C++ ('Rcpp',
'RcppArmadillo') and 'data.table', scaling to pedigrees with over one
million individuals. Pedigree graphs are rendered via 'igraph' with
support for compact full-sib family display; relationship matrices can be
visualized as heatmaps. Supports complex mating systems, including selfing
and pedigrees in which the same individual can appear as both sire and
dam.

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
