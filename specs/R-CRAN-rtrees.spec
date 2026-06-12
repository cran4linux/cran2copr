%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtrees
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Deriving Phylogenies from Synthesis Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-megatrees >= 0.1.3
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-tidytree 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-castor 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-megatrees >= 0.1.3
Requires:         R-CRAN-ape 
Requires:         R-CRAN-tidytree 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-castor 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Rcpp 

%description
Provides tools to derive species-level phylogenies from large synthesis
mega-trees for a wide range of taxonomic groups, including plants, birds,
mammals, amphibians, reptiles, fish, bees, butterflies, and sharks. When a
queried species is absent from the mega-tree, it is grafted onto the tree
using one of two placement strategies: attachment at the basal node of the
most closely related genus or family ('at_basal_node'), or random
attachment below that basal node with probability proportional to branch
length ('random_below_basal'). See Li (2023) <doi:10.1111/ecog.06643> for
details. Multiple species from a genus not represented in the mega-tree
are placed as a polytomy to preserve clade coherence. The package
interfaces with the 'megatrees' data package, which bundles or downloads
on demand curated mega-trees. Users can also provide their own mega-trees.

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
