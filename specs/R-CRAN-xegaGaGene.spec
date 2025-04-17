%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xegaGaGene
%global packver   1.0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Binary Gene Operations for Genetic Algorithms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xegaSelectGene 
Requires:         R-CRAN-xegaSelectGene 

%description
Representation-dependent gene level operations of a genetic algorithm with
binary coded genes: Initialization of random binary genes, several gene
maps for binary genes, several mutation operators, several crossover
operators with 1 and 2 kids, replication pipelines for 1 and 2 kids, and,
last but not least, function factories for configuration. See Goldberg, D.
E. (1989, ISBN:0-201-15767-5). For crossover operators, see Syswerda, G.
(1989, ISBN:1-55860-066-3), Spears, W. and De Jong, K. (1991,
ISBN:1-55860-208-9). For mutation operators, see Stanhope, S. A. and
Daida, J. M. (1996, ISBN:0-18-201-031-7).

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
