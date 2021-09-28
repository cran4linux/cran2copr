%global __brp_check_rpaths %{nil}
%global packname  EnvNJ
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Whole Genome Phylogenies Using Sequence Environments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-bio3d 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-philentropy 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-bio3d 
Requires:         R-graphics 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-philentropy 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-stringr 

%description
Contains utilities for the analysis of protein sequences in a phylogenetic
context. Allows the generation of phylogenetic trees base on protein
sequences in an alignment-independent way. Two different methods have been
implemented. One approach is based on the frequency analysis of n-grams,
previously described in Stuart et al. (2002)
<doi:10.1093/bioinformatics/18.1.100>. The other approach is based on the
species-specific neighborhood preference around amino acids. Features
include the conversion of a protein set into a vector reflecting these
neighborhood preferences, pairwise distances (dissimilarity) between these
vectors, and the generation of trees based on these distance matrices.

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
