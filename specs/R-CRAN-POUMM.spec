%global packname  POUMM
%global packver   2.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          The Phylogenetic Ornstein-Uhlenbeck Mixed Model

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-data.table >= 1.13.2
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lamW 
BuildRequires:    R-CRAN-adaptMCMC 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table >= 1.13.2
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lamW 
Requires:         R-CRAN-adaptMCMC 
Requires:         R-utils 

%description
The Phylogenetic Ornstein-Uhlenbeck Mixed Model (POUMM) allows to estimate
the phylogenetic heritability of continuous traits, to test hypotheses of
neutral evolution versus stabilizing selection, to quantify the strength
of stabilizing selection, to estimate measurement error and to make
predictions about the evolution of a phenotype and phenotypic variation in
a population. The package implements combined maximum likelihood and
Bayesian inference of the univariate Phylogenetic Ornstein-Uhlenbeck Mixed
Model, fast parallel likelihood calculation, maximum likelihood inference
of the genotypic values at the tips, functions for summarizing and
plotting traces and posterior samples, functions for simulation of a
univariate continuous trait evolution model along a phylogenetic tree. So
far, the package has been used for estimating the heritability of
quantitative traits in macroevolutionary and epidemiological studies, see
e.g. Bertels et al. (2017) <doi:10.1093/molbev/msx246> and Mitov and
Stadler (2018) <doi:10.1093/molbev/msx328>. The algorithm for parallel
POUMM likelihood calculation has been published in Mitov and Stadler
(2019) <doi:10.1111/2041-210X.13136>.

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
