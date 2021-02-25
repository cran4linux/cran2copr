%global packname  ratematrix
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimation of the Evolutionary Rate Matrix

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-phylolm 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-mvMORPH 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-phylolm 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-mvMORPH 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ellipse 

%description
The Evolutionary Rate Matrix is a variance-covariance matrix which
describes both the rates of trait evolution and the evolutionary
correlation among multiple traits. This package has functions to estimate
these parameters using Bayesian MCMC. It is possible to test if the
pattern of evolutionary correlations among traits has changed between
predictive regimes painted along the branches of the phylogenetic tree.
Regimes can be created a priori or estimated as part of the MCMC under a
joint estimation approach. The package has functions to run MCMC chains,
plot results, evaluate convergence, and summarize posterior distributions.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
