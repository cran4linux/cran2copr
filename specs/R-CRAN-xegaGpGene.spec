%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xegaGpGene
%global packver   1.0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Genetic Operations for Grammar-Based Genetic Programming

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xegaBNF 
BuildRequires:    R-CRAN-xegaDerivationTrees 
BuildRequires:    R-CRAN-xegaSelectGene 
Requires:         R-stats 
Requires:         R-CRAN-xegaBNF 
Requires:         R-CRAN-xegaDerivationTrees 
Requires:         R-CRAN-xegaSelectGene 

%description
An implementation of the representation-dependent gene level operations of
grammar-based genetic programming with genes which are derivation trees of
a context-free grammar: Initialization of a gene with a complete random
derivation tree, decoding of a derivation tree. Crossover is implemented
by exchanging subtrees. Depth-bounds for the minimal and the maximal depth
of the roots of the subtrees exchanged by crossover can be set. Mutation
is implemented by replacing a subtree by a random subtree. The depth of
the random subtree and the insertion node are configurable. For details,
see Geyer-Schulz (1997, ISBN:978-3-7908-0830-X).

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
