%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glymotif
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extract Glycan Motifs from Glycan Structures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-glyrepr >= 1.0.0
BuildRequires:    R-CRAN-glyparse >= 0.6.0
BuildRequires:    R-CRAN-glydraw >= 0.4.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-glyrepr >= 1.0.0
Requires:         R-CRAN-glyparse >= 0.6.0
Requires:         R-CRAN-glydraw >= 0.4.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-Rcpp 

%description
Identify, count, and match recurring substructures in glycan structures.
Supports concrete and generic monosaccharide matching, several structural
alignment modes, node-to-node mappings, and batch analysis using subgraph
isomorphism. Includes curated motif annotations derived from the
'GlycoMotif' resource <https://glycomotif.glyomics.org/>. Integrates with
'glyrepr' and 'glyparse' for structural glycomics workflows.

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
