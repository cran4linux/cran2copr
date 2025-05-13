%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  graphsim
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Expression Data from 'igraph' Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-graphics 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-Matrix 
Requires:         R-graphics 

%description
Functions to develop simulated continuous data (e.g., gene expression)
from a sigma covariance matrix derived from a graph structure in 'igraph'
objects. Intended to extend 'mvtnorm' to take 'igraph' structures rather
than sigma matrices as input. This allows the use of simulated data that
correctly accounts for pathway relationships and correlations. This allows
the use of simulated data that correctly accounts for pathway
relationships and correlations. Here we present a versatile statistical
framework to simulate correlated gene expression data from biological
pathways, by sampling from a multivariate normal distribution derived from
a graph structure. This package allows the simulation of biological
pathways from a graph structure based on a statistical model of gene
expression. For example methods to infer biological pathways and gene
regulatory networks from gene expression data can be tested on simulated
datasets using this framework. This also allows for pathway structures to
be considered as a confounding variable when simulating gene expression
data to test the performance of genomic analyses.

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
