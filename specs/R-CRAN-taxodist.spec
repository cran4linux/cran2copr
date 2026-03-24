%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  taxodist
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Taxonomic Distance and Phylogenetic Lineage Computation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-rvest >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-rvest >= 1.0.0
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-utils 
Requires:         R-stats 

%description
Computes phylogenetic distances between any two taxa using hierarchical
lineage data retrieved from The Taxonomicon
<http://taxonomicon.taxonomy.nl>, a comprehensive curated classification
of all life based on Systema Naturae 2000 (Brands, 1989
<http://taxonomicon.taxonomy.nl>). Given any two taxon names, retrieves
their full lineages, identifies the most recent common ancestor (MRCA),
and computes a dissimilarity index based on the depth of the most recent
common ancestor. Supports individual distance queries, pairwise distance
matrices, clade filtering, and lineage utilities.

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
