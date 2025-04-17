%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xegaDerivationTrees
%global packver   1.0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Generating and Manipulating Derivation Trees

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xegaBNF 
Requires:         R-CRAN-xegaBNF 

%description
Derivation tree operations are needed for implementing grammar-based
genetic programming and grammatical evolution: Generating a random
derivation trees of a context-free grammar of bounded depth, decoding a
derivation tree, choosing a random node in a derivation tree, extracting a
tree whose root is a specified node, and inserting a subtree into a
derivation tree at a specified node. These operations are necessary for
the initialization and for decoders of a random population of programs, as
well as for implementing crossover and mutation operators. Depth-bounds
are guaranteed by switching to a grammar without recursive production
rules. For executing the examples, the package 'BNF' is needed. The basic
tree operations for generating, extracting, and inserting derivation trees
as well as the conditions for guaranteeing complete derivation trees have
been presented in Geyer-Schulz (1997, ISBN:978-3-7908-0830-X). The use of
random integer vectors for the generation of derivation trees has been
introduced in Ryan, C., Collins, J. J., and O'Neill, M. (1998)
<doi:10.1007/BFb0055930> for grammatical evolution.

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
