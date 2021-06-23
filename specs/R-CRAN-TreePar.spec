%global __brp_check_rpaths %{nil}
%global packname  TreePar
%global packver   3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3
Release:          2%{?dist}%{?buildtag}
Summary:          Estimating birth and death rates based on phylogenies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-TreeSim >= 2.1
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-TreeSim >= 2.1
Requires:         R-CRAN-ape 
Requires:         R-Matrix 
Requires:         R-CRAN-subplex 
Requires:         R-CRAN-deSolve 

%description
(i) For a given species phylogeny on present day data which is calibrated
to calendar-time, a method for estimating maximum likelihood speciation
and extinction processes is provided. The method allows for non-constant
rates. Rates may change (1) as a function of time, i.e. rate shifts at
specified times or mass extinction events (likelihood implemented as
LikShifts, optimization as bd.shifts.optim and visualized as
bd.shifts.plot) or (2) as a function of the number of species, i.e.
density-dependence (likelihood implemented as LikDD and optimization as
bd.densdep.optim) or (3) extinction rate may be a function of species age
(likelihood implemented as LikAge and optimization as
bd.age.optim.matlab). Note that the methods take into account the whole
phylogeny, in particular it accounts for the "pull of the present" effect.
(1-3) can take into account incomplete species sampling, as long as each
species has the same probability of being sampled. For a given phylogeny
on higher taxa (i.e. all but one species per taxa are missing), where the
number of species is known within each higher taxa, speciation and
extinction rates can be estimated under model (1) (implemented within
LikShifts and bd.shifts.optim with groups !=0). (ii) For a given phylogeny
with sequentially sampled tips, e.g. a virus phylogeny, rates can be
estimated under a model where rates vary across time using bdsky.stt.optim
based on likelihood LikShiftsSTT (extending LikShifts and
bd.shifts.optim). Furthermore, rates may vary as a function of host types
using LikTypesSTT (multitype branching process extending functions in R
package diversitree). This function can furthermore calculate the
likelihood under an epidemiological model where infected individuals are
first exposed and then infectious.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
