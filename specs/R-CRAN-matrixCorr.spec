%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  matrixCorr
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Correlation and Association Estimators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-Matrix >= 1.7.2
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-cpp11 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-Matrix >= 1.7.2
Requires:         R-CRAN-Rcpp >= 1.1.0

%description
Compute correlation and other association matrices from small to
high-dimensional datasets with relative simple functions and sensible
defaults. Includes options for shrinkage and robustness to improve results
in noisy or high-dimensional settings (p >= n), plus convenient print/plot
methods for inspection. Implemented with optimised C++ backends using
BLAS/OpenMP and memory-aware symmetric updates. Works with base matrices
and data frames, returning standard R objects via a consistent S3
interface. Useful across genomics, agriculture, and machine-learning
workflows. Supports Pearson, Spearman, Kendall, distance correlation,
partial correlation, and robust biweight mid-correlation; Bland–Altman
analyses and Lin's concordance correlation coefficient (including
repeated-measures extensions). Methods based on Ledoit and Wolf (2004)
<doi:10.1016/S0047-259X(03)00096-4>; Schäfer and Strimmer (2005)
<doi:10.2202/1544-6115.1175>; Lin (1989) <doi:10.2307/2532051>.

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
