%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastphylosig
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Phylogenetic Signal Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ape 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Provides one-command and method-specific workflows for phylogenetic signal
in continuous, binary, and categorical traits. Compiled tree-pruning
algorithms implement Blomberg's K and Pagel's lambda without constructing
a dense phylogenetic covariance matrix in production. Fritz and Purvis D
retains separate random and Brownian null models, while categorical Delta
combines discrete ancestral-state likelihoods with MCMC and permutation
diagnostics. The package also provides reusable prepared trees, explicit
tree/data matching, trait-wise missing-value handling, conservative tree
diagnostics, bounded simulation memory, and structured timing and Monte
Carlo uncertainty metadata. Methods follow Blomberg, Garland and Ives
(2003) <doi:10.1111/j.0014-3820.2003.tb00285.x> for K, Pagel (1999)
<doi:10.1038/44766> for lambda, Fritz and Purvis (2010)
<doi:10.1111/j.1523-1739.2010.01455.x> for D, and Borges et al. (2019)
<doi:10.1093/bioinformatics/bty800> for categorical Delta.

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
