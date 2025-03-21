%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phytools
%global packver   2.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Tools for Comparative Biology (and Other Things)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.7
BuildRequires:    R-CRAN-phangorn >= 2.3.1
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape >= 5.7
Requires:         R-CRAN-phangorn >= 2.3.1
Requires:         R-CRAN-maps 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-optimParallel 
Requires:         R-parallel 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-stats 
Requires:         R-utils 

%description
A wide range of methods for phylogenetic analysis - concentrated in
phylogenetic comparative biology, but also including numerous techniques
for visualizing, analyzing, manipulating, reading or writing, and even
inferring phylogenetic trees. Included among the functions in phylogenetic
comparative biology are various for ancestral state reconstruction,
model-fitting, and simulation of phylogenies and trait data. A broad range
of plotting methods for phylogenies and comparative data include (but are
not restricted to) methods for mapping trait evolution on trees, for
projecting trees into phenotype space or a onto a geographic map, and for
visualizing correlated speciation between trees. Lastly, numerous
functions are designed for reading, writing, analyzing, inferring,
simulating, and manipulating phylogenetic trees and comparative data. For
instance, there are functions for computing consensus phylogenies from a
set, for simulating phylogenetic trees and data under a range of models,
for randomly or non-randomly attaching species or clades to a tree, as
well as for a wide range of other manipulations and analyses that
phylogenetic biologists might find useful in their research.

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
