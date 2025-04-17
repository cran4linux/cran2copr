%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xegaPermGene
%global packver   1.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Operations on Permutation Genes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xegaSelectGene 
Requires:         R-CRAN-xegaSelectGene 

%description
An implementation of representation-dependent gene level operations for
genetic algorithms with genes representing permutations: Initialization of
genes, mutation, and crossover. The crossover operation provided is
position-based crossover (Syswerda, G., Chap. 21 in Davis, L. (1991,
ISBN:0-442-00173-8). For mutation, several variants are included:
Order-based mutation (Syswerda, G., Chap. 21 in Davis, L. (1991,
ISBN:0-442-00173-8), randomized Lin-Kernighan heuristics (Croes, G. A.
(1958) <doi:10.1287/opre.6.6.791> and Lin, S. and Kernighan. B. W. (1973)
<doi:10.1287/opre.21.2.498>), and randomized greedy operators. A random
mix operator for mutation selects a mutation variant randomly.

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
