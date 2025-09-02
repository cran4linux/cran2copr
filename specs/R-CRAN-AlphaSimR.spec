%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AlphaSimR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Breeding Program Simulations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.500.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rdpack 

%description
The successor to the 'AlphaSim' software for breeding program simulation
[Faux et al. (2016) <doi:10.3835/plantgenome2016.02.0013>]. Used for
stochastic simulations of breeding programs to the level of DNA sequence
for every individual. Contained is a wide range of functions for modeling
common tasks in a breeding program, such as selection and crossing. These
functions allow for constructing simulations of highly complex plant and
animal breeding programs via scripting in the R software environment. Such
simulations can be used to evaluate overall breeding program performance
and conduct research into breeding program design, such as implementation
of genomic selection. Included is the 'Markovian Coalescent Simulator'
('MaCS') for fast simulation of biallelic sequences according to a
population demographic history [Chen et al. (2009)
<doi:10.1101/gr.083634.108>].

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
