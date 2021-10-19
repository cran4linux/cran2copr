%global __brp_check_rpaths %{nil}
%global packname  BAMMtools
%global packver   2.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Visualization of Macroevolutionary Dynamics on Phylogenetic Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-ape 
Requires:         R-CRAN-gplots 
Requires:         R-methods 

%description
Provides functions for analyzing and visualizing complex macroevolutionary
dynamics on phylogenetic trees. It is a companion package to the command
line program BAMM (Bayesian Analysis of Macroevolutionary Mixtures) and is
entirely oriented towards the analysis, interpretation, and visualization
of evolutionary rates. Functionality includes visualization of rate shifts
on phylogenies, estimating evolutionary rates through time, comparing
posterior distributions of evolutionary rates across clades, comparing
diversification models using Bayes factors, and more.

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
