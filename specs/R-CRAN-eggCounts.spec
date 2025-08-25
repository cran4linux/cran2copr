%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eggCounts
%global packver   2.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Modelling of Faecal Egg Counts

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.1.4
BuildRequires:    R-CRAN-rstantools >= 2.3.1
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-rstan >= 2.26
BuildRequires:    R-CRAN-BH >= 1.75.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.9.1
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-rstantools >= 2.3.1
Requires:         R-CRAN-rstan >= 2.26
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-rstantools

%description
An implementation of Bayesian hierarchical models for faecal egg count
data to assess anthelmintic efficacy. Bayesian inference is done via MCMC
sampling using 'Stan' <https://mc-stan.org/>.

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
