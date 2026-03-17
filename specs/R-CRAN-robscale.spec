%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robscale
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Accelerated Estimation of Robust Location and Scale

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppParallel >= 5.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-RcppParallel >= 5.0.0
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Estimates robust location and scale parameters using platform-specific
Single Instruction, Multiple Data (SIMD) vectorization and Intel Threading
Building Blocks (TBB) for parallel processing. Implements a novel
variance-weighted ensemble estimator that adaptively combines all
available statistics. Included methods feature logistic M-estimators, the
estimators of Rousseeuw and Croux (1993), the Gini mean difference, the
scaled Median Absolute Deviation (MAD), the scaled Interquartile Range
(IQR), and unbiased standard deviations. Achieves substantial speedups
over existing implementations through an 'Rcpp' backend and a unified
dispatcher that automatically selects the optimal estimator based on
sample size.

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
