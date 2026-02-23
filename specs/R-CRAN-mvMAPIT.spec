%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mvMAPIT
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Genome Wide Marginal Epistasis Test

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-harmonicmeanp 
BuildRequires:    R-CRAN-logging 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppSpdlog 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-harmonicmeanp 
Requires:         R-CRAN-logging 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-truncnorm 
Requires:         R-utils 

%description
Epistasis, commonly defined as the interaction between genetic loci, is
known to play an important role in the phenotypic variation of complex
traits. As a result, many statistical methods have been developed to
identify genetic variants that are involved in epistasis, and nearly all
of these approaches carry out this task by focusing on analyzing one trait
at a time. Previous studies have shown that jointly modeling multiple
phenotypes can often dramatically increase statistical power for
association mapping. In this package, we present the 'multivariate
MArginal ePIstasis Test' ('mvMAPIT') – a multi-outcome generalization of a
recently proposed epistatic detection method which seeks to detect
marginal epistasis or the combined pairwise interaction effects between a
given variant and all other variants. By searching for marginal epistatic
effects, one can identify genetic variants that are involved in epistasis
without the need to identify the exact partners with which the variants
interact – thus, potentially alleviating much of the statistical and
computational burden associated with conventional explicit search based
methods. Our proposed 'mvMAPIT' builds upon this strategy by taking
advantage of correlation structure between traits to improve the
identification of variants involved in epistasis. We formulate 'mvMAPIT'
as a multivariate linear mixed model and develop a multi-trait variance
component estimation algorithm for efficient parameter inference and
P-value computation. Together with reasonable model approximations, our
proposed approach is scalable to moderately sized genome-wide association
studies. Crawford et al. (2017) <doi:10.1371/journal.pgen.1006869>. Stamp
et al. (2023) <doi:10.1093/g3journal/jkad118>. Stamp et al. (2025)
<doi:10.1016/j.ajhg.2025.07.004>.

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
