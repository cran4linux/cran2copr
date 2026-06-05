%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phyloatlas
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access to the 'Phylo-Species Atlas' of Empirical Phylogenies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape 
Requires:         R-utils 

%description
Provides convenience functions to fetch standardized phylogenetic trees
and per-tree provenance metadata from the 'Phylo-Species Atlas'
<https://github.com/franciscorichter/phylo-species-atlas> directly from R.
The atlas is a curated collection of empirical species-level trees
covering Bacteria, Archaea, and Eukaryota, organized into 62 partitions of
life with tip labels normalized against a shared dictionary of
standardized species identifiers. Functions load any of the standardized
trees with species labels resolved from the dictionary, list available
trees, and inspect per-tree provenance.

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
