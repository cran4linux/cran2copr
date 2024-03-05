%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coala
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework for Coalescent Simulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-rehh >= 3.0.0
BuildRequires:    R-CRAN-R6 >= 2.0.1
BuildRequires:    R-CRAN-scrm >= 1.6.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.3.810.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rehh >= 3.0.0
Requires:         R-CRAN-R6 >= 2.0.1
Requires:         R-CRAN-scrm >= 1.6.0.2
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-CRAN-digest 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Coalescent simulators can rapidly simulate biological sequences evolving
according to a given model of evolution. You can use this package to
specify such models, to conduct the simulations and to calculate
additional statistics from the results (Staab, Metzler, 2016
<doi:10.1093/bioinformatics/btw098>). It relies on existing simulators for
doing the simulation, and currently supports the programs 'ms', 'msms' and
'scrm'. It also supports finite-sites mutation models by combining the
simulators with the program 'seq-gen'. Coala provides functions for
calculating certain summary statistics, which can also be applied to
actual biological data. One possibility to import data is through the
'PopGenome' package (<https://github.com/pievos101/PopGenome>).

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
