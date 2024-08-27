%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SIMplyBee
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          'AlphaSimR' Extension for Simulating Honeybee Populations and Breeding Programmes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-extraDistr >= 1.9.1
BuildRequires:    R-CRAN-AlphaSimR >= 1.5.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.500.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-extraDistr >= 1.9.1
Requires:         R-CRAN-AlphaSimR >= 1.5.3
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-RANN 

%description
An extension of the 'AlphaSimR' package
(<https://cran.r-project.org/package=AlphaSimR>) for stochastic
simulations of honeybee populations and breeding programmes. 'SIMplyBee'
enables simulation of individual bees that form a colony, which includes a
queen, fathers (drones the queen mated with), virgin queens, workers, and
drones. Multiple colony can be merged into a population of colonies, such
as an apiary or a whole country of colonies. Functions enable operations
on castes, colony, or colonies, to ease 'R' scripting of whole
populations. All 'AlphaSimR' functionality with respect to genomes and
genetic and phenotype values is available and further extended for
honeybees, including haplo-diploidy, complementary sex determiner locus,
colony events (swarming, supersedure, etc.), and colony phenotype values.

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
