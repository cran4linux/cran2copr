%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xega
%global packver   0.9.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Evolutionary and Genetic Algorithms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-xegaSelectGene 
BuildRequires:    R-CRAN-xegaBNF 
BuildRequires:    R-CRAN-xegaDerivationTrees 
BuildRequires:    R-CRAN-xegaGaGene 
BuildRequires:    R-CRAN-xegaGpGene 
BuildRequires:    R-CRAN-xegaGeGene 
BuildRequires:    R-CRAN-xegaDfGene 
BuildRequires:    R-CRAN-xegaPermGene 
BuildRequires:    R-CRAN-xegaPopulation 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-xegaSelectGene 
Requires:         R-CRAN-xegaBNF 
Requires:         R-CRAN-xegaDerivationTrees 
Requires:         R-CRAN-xegaGaGene 
Requires:         R-CRAN-xegaGpGene 
Requires:         R-CRAN-xegaGeGene 
Requires:         R-CRAN-xegaDfGene 
Requires:         R-CRAN-xegaPermGene 
Requires:         R-CRAN-xegaPopulation 

%description
Implementation of a scalable, highly configurable, and e(x)tended
architecture for (e)volutionary and (g)enetic (a)lgorithms. Multiple
representations (binary, real-coded, permutation, and derivation-tree), a
rich collection of genetic operators, as well as an extended processing
pipeline are provided for genetic algorithms (Goldberg, D. E. (1989,
ISBN:0-201-15767-5)), differential evolution (Price, Kenneth V., Storn,
Rainer M. and Lampinen, Jouni A. (2005) <doi:10.1007/3-540-31306-0>),
simulated annealing (Aarts, E., and Korst, J. (1989, ISBN:0-471-92146-7)),
grammar-based genetic programming (Geyer-Schulz (1997,
ISBN:978-3-7908-0830-X)), and grammatical evolution (Ryan, C., O'Neill,
M., and Collins, J. J. (2018) <doi:10.1007/978-3-319-78717-6>). All
algorithms reuse basic adaptive mechanisms for performance optimization.
Sequential or parallel execution (on multi-core machines, local clusters,
and high performance computing environments) is available for all
algorithms. See
<https://github.com/ageyerschulz/xega/tree/main/examples/executionModel>.

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
