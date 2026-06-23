%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  momst
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Objective Minimum Spanning Tree via NSGA-II with Local Search

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Solves the Multi-Criteria Minimum Spanning Tree (mc-MST) problem on
complete weighted graphs by combining the Non-dominated Sorting Genetic
Algorithm II (NSGA-II) with optional Pareto local search operators.
Chromosomes are represented as Prufer sequences so that every random
individual decodes to a valid spanning tree (Cayley's theorem), avoiding
repair operators. Four solver variants are provided: pure NSGA-II
("base"), Path Relinking ("PR"), Pareto Local Search ("PLS"), and Tabu
Search ("TS"). The package supports 2 and 3 objective formulations and
provides convenience functions to plot Pareto fronts and best-compromise
spanning trees. This package is the reference implementation of the method
described in Parraga-Alava, Inostroza-Ponta and Dorn (2017)
<doi:10.1109/CEC.2017.7969432>.

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
