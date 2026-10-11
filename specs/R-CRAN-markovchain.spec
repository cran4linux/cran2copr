%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  markovchain
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Handling Discrete Time Markov Chains

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.600.4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-stats4 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-expm 
Requires:         R-stats4 
Requires:         R-parallel 
Requires:         R-CRAN-RcppParallel 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Description: Functions and S4 classes to create, manage and analyse
discrete time Markov chains. Includes probabilistic analysis of chain
structure (state classification, hitting times, stationary distributions,
spectral and mixing diagnostics), statistical inference (maximum
likelihood and Bayesian estimation, tests of the Markov property,
homogeneity, stationarity and order, simulation), higher-order and
multivariate chains, state aggregation, and import/export to JSON, YAML
and CSV. Basic support for continuous time Markov chains is also provided;
some of these functions depend on the suggested 'ctmcd' package. See
Spedicato (2017) <doi:10.32614/RJ-2017-036>.

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
