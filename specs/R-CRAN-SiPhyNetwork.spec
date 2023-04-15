%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SiPhyNetwork
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Phylogenetic Simulator for Reticulate Evolution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rstackdeque 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-stats 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rstackdeque 
Requires:         R-CRAN-lifecycle 

%description
A simulator for reticulate evolution under a birth-death-hybridization
process. Here the birth-death process is extended to consider reticulate
Evolution by allowing hybridization events to occur. The general purpose
simulator allows the modeling of three different reticulate patterns:
lineage generative hybridization, lineage neutral hybridization, and
lineage degenerative hybridization. Users can also specify hybridization
events to be dependent on a trait value or genetic distance. We also
extend some phylogenetic tree utility and plotting functions for networks.
We allow two different stopping conditions: simulated to a fixed time or
number of taxa. When simulating to a fixed number of taxa, the user can
simulate under the Generalized Sampling Approach that properly simulates
phylogenies when assuming a uniform prior on the root age.

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
