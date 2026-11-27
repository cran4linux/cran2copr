%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  taxodist
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Taxonomic Hierarchy Distances and Lineage Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.3.0
BuildRequires:    R-CRAN-rvest >= 1.0.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.3.0
Requires:         R-CRAN-rvest >= 1.0.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-tools 

%description
Computes distances between taxonomic hierarchy nodes using lineage data
retrieved from The Taxonomicon <http://taxonomicon.taxonomy.nl>, the Open
Tree of Life reference taxonomy (Rees and Cranston, 2017)
<doi:10.3897/BDJ.5.e12581>, or the NCBI Taxonomy (Schoch et al., 2020)
<doi:10.1093/database/baaa062>. For distinct nodes, distance is defined as
the reciprocal of the depth of their most recent common ancestor;
identical nodes have distance zero. This definition yields an ultrametric
within each connected hierarchy. Path length, Wu-Palmer, and rank-based
distances are also available, together with the taxonomic diversity and
distinctness indices of Clarke and Warwick (1998)
<doi:10.1046/j.1365-2664.1998.3540523.x> and their randomization test, the
taxonomic dissimilarities between samples of Clarke, Somerfield and
Chapman (2006) <doi:10.1016/j.jembe.2005.12.017>, and standardized effect
sizes of mean pairwise and nearest-taxon distances (Webb et al., 2002)
<doi:10.1146/annurev.ecolsys.33.010802.150448>. Functions are provided for
auditable name resolution, comparison of classifications, online or
user-supplied lineage analysis, node ranks, clade membership, pairwise,
matrix, and cross-set distance calculation, classification trees with
named clades, hierarchical clustering, principal coordinates analysis,
portable and comparable JSON analysis bundles, and cache management.
Distance matrices are returned as base R 'dist' objects. The distances
represent classification depth rather than evolutionary time or
phylogenetic branch length.

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
