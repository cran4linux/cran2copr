%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phylopairs
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Comparative Analyses of Lineage-Pair Traits

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.4.0
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-ape 
Requires:         R-CRAN-loo 
Requires:         R-methods 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-rstantools

%description
Facilitates the testing of causal relationships among lineage-pair traits
in a phylogenetically informed context. Lineage-pair traits are characters
that are defined for pairs of lineages instead of individual taxa.
Examples include the strength of reproductive isolation, range overlap,
competition coefficient, diet niche similarity, and relative hybrid
fitness. Users supply a lineage-pair dataset and a phylogeny. 'phylopairs'
calculates a covariance matrix for the pairwise-defined data and provides
built-in models to test for relationships among variables while taking
this covariance into account. Bayesian sampling is run through built-in
'Stan' programs via the 'rstan' package. The various models and methods
that this package makes available are described in Anderson et al. (In
Review), Coyne and Orr (1989) <doi:10.1111/j.1558-5646.1989.tb04233.x>,
Fitzpatrick (2002) <doi:10.1111/j.0014-3820.2002.tb00860.x>, and Castillo
(2007) <doi:10.1002/ece3.3093>.

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
