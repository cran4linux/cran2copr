%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bgms
%global packver   0.2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Graphical Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-S7 
Requires:         R-methods 
Requires:         R-CRAN-lifecycle 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Bayesian estimation and edge selection for graphical models of mixed
binary, ordinal, and continuous variables. The variable types determine
the model: an ordinal Markov random field for discrete data, a Gaussian
graphical model for continuous data, or a mixed Markov random field
combining both. Edge inclusion is determined through spike-and-slab
priors, yielding posterior inclusion probabilities for each edge. Supports
multi-group comparison via 'bgmCompare()', simulation, prediction, and
missing data imputation.

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
