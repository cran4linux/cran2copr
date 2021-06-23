%global __brp_check_rpaths %{nil}
%global packname  treeducken
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nested Phylogenetic Tree Simulator

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-apTreeshape 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-ape 
Requires:         R-CRAN-apTreeshape 
Requires:         R-graphics 
Requires:         R-methods 

%description
Simulates nested phylogenetic trees (gene trees in species tree, symbiont
trees in host trees) using birth-death processes and transfers between
lineages. Simulations of gene trees within species trees are performed
using a three-tree model with species trees, locus trees, and gene trees.
The cophylogenetic birth-death process is used to simulate sets of host
and symbiont trees with extant associations between tips. For more
information about the three-tree model see: Mallo et al. (2015)
<doi:10.1093/sysbio/syv082>, Rasmussen and Kellis (2012)
<doi:10.1101/gr.123901.111>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
