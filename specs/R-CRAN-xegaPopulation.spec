%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xegaPopulation
%global packver   1.0.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Genetic Population Level Functions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xegaGaGene 
BuildRequires:    R-CRAN-xegaSelectGene 
Requires:         R-parallel 
Requires:         R-CRAN-future.apply 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-xegaGaGene 
Requires:         R-CRAN-xegaSelectGene 

%description
This collection of gene representation-independent functions implements
the population layer of extended evolutionary and genetic algorithms and
its support. The population layer consists of functions for initializing,
logging, observing, evaluating a population of genes, as well as of
computing the next population. For parallel evaluation of a population of
genes 4 execution models - named Sequential, MultiCore, FutureApply, and
Cluster - are provided. They are implemented by configuring the lapply()
function. The execution model FutureApply can be externally configured as
recommended by Bengtsson (2021) <doi:10.32614/RJ-2021-048>. Configurable
acceptance rules and cooling schedules (see Kirkpatrick, S., Gelatt, C. D.
J, and Vecchi, M. P. (1983) <doi:10.1126/science.220.4598.671>, and Aarts,
E., and Korst, J. (1989, ISBN:0-471-92146-7) offer simulated annealing or
greedy randomized approximate search procedure elements. Adaptive
crossover and mutation rates depending on population statistics generalize
the approach of Stanhope, S. A. and Daida, J. M. (1996,
ISBN:0-18-201-031-7).

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
