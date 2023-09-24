%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cloneRate
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Growth Rates from Phylogenetic Trees

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-ape >= 4.0
BuildRequires:    R-CRAN-rstantools >= 2.3.1
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-Rmpfr >= 0.8
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-ape >= 4.0
Requires:         R-CRAN-rstantools >= 2.3.1
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rmpfr >= 0.8
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
Quickly estimate the net growth rate of a population or clone whose growth
can be approximated by a birth-death branching process.  Input should be
phylogenetic tree(s) of clone(s) with edge lengths corresponding to either
time or mutations. Based on coalescent results in Johnson et al. (2023)
<doi:10.1093/bioinformatics/btad561>. Simulation techniques as well as
growth rate methods build on prior work from Lambert A. (2018)
<doi:10.1016/j.tpb.2018.04.005> and Stadler T. (2009)
<doi:10.1016/j.jtbi.2009.07.018>.

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
