%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  matrixCorr
%global packver   0.12.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.2
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Correlation, Agreement, and Reliability Estimators

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-Matrix >= 1.7.2
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-Matrix >= 1.7.2
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-rlang 

%description
Compute correlation, association, agreement, and reliability measures for
small to high-dimensional datasets through a consistent matrix-oriented
interface. Supports classical correlations (Pearson, Spearman, Kendall,
Chatterjee's rank correlation), distance correlation, partial correlation
with regularised estimators, shrinkage correlation for p >= n settings,
robust correlations including biweight mid-correlation, percentage-bend,
Winsorized, and skipped correlation, latent-variable methods for binary
and ordinal data, pairwise and overall intraclass correlation for wide
data, repeated-measures correlation, and agreement/reliability analyses
based on Cohen's kappa, weighted kappa, multi-rater kappa, Gwet's AC1/AC2,
Krippendorff's alpha, Bland-Altman methods, Lin's concordance correlation
coefficient, Poisson GLMM concordance for count data, and
repeated-measures intraclass/concordance correlation. Implemented with
optimized C++ backends using BLAS/OpenMP and memory-aware symmetric
updates, and returns standard R objects with print/summary/plot methods
plus optional Shiny viewers for matrix inspection. Methods based on Ledoit
and Wolf (2004) <doi:10.1016/S0047-259X(03)00096-4>; high-dimensional
shrinkage covariance estimation <doi:10.2202/1544-6115.1175>; Lin (1989)
<doi:10.2307/2532051>; Wilcox (1994) <doi:10.1007/BF02294395>; Wilcox
(2004) <doi:10.1080/0266476032000148821>; Hayes and Krippendorff (2007)
<doi:10.1080/19312450709336664>; weighted repeated-measures correlation by
Kondo et al. (2025) <doi:10.1002/sim.70046>.

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
