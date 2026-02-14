%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xegaSelectGene
%global packver   1.0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Selection of Genes and Gene Representation Independent Functions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
This collection of gene representation-independent mechanisms for
evolutionary and genetic algorithms for the R-package xega
<https://CRAN.R-project.org/package=xega> contains four groups of
functions: First, functions for selecting a gene in a population of genes
according to its fitness value and for adaptive scaling of the fitness
values as well as for performance optimization and measurement offer
several variants for implementing the survival of the fittest. Second,
evaluation functions for deterministic functions avoid recomputation.
Evaluation of stochastic functions incrementally improve the estimation of
the mean and variance of fitness values at almost no additional cost.
Evaluation functions for gene repair handle error-correcting decoders.
Third, timing and counting functions for profiling the algorithm pipeline
are provided to assess bottlenecks in the algorithms. Fourth, a small
collection of problem environments for function optimization,
combinatorial optimization, and grammar-based genetic programming and
grammatical evolution is provided for tutorial examples. For xega's
architecture, see Geyer-Schulz, A. (2025) <doi:10.5445/IR/1000187255>. The
methods in the package are described by the following references: Baker,
James E. (1987, ISBN:978-08058-0158-8), De Jong, Kenneth A. (1975)
<https://deepblue.lib.umich.edu/handle/2027.42/4507>, Geyer-Schulz,
Andreas (1997, ISBN:978-3-7908-0830-X), Grefenstette, John J. (1987,
ISBN:978-08058-0158-8), Grefenstette, John J. and Baker, James E. (1989,
ISBN:1-55860-066-3), Holland, John (1975, ISBN:0-472-08460-7), Lau, H. T.
(1986) <doi:10.1007/978-3-642-61649-5>, Price, Kenneth V., Storn, Rainer
M. and Lampinen, Jouni A. (2005) <doi:10.1007/3-540-31306-0>, Reynolds, J.
C. (1993) <doi:10.1007/BF01019459>, Schaffer, J. David (1989,
ISBN:1-55860-066-3), Wenstop, Fred (1980)
<doi:10.1016/0165-0114(80)90031-7>, Whitley, Darrell (1989,
ISBN:1-55860-066-3), Wickham, Hadley (2019, ISBN:978-815384571).

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
