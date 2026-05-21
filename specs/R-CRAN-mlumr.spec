%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlumr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multilevel Unanchored Meta-Regression for Indirect Treatment Comparisons

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstantools >= 2.3.0
BuildRequires:    R-CRAN-rstan >= 2.26.0
BuildRequires:    R-CRAN-StanHeaders >= 2.26.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.3.0
Requires:         R-CRAN-rstan >= 2.26.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-rstantools

%description
Bayesian multilevel unanchored meta-regression (ML-UMR) for indirect
treatment comparisons using individual patient data (IPD) and aggregate
data (AgD). Implements shared prognostic factor assumption (SPFA) and
relaxed SPFA models for binary, continuous, and count outcomes via 'Stan'.
Also provides simulated treatment comparison (STC) via parametric
G-computation and naive unadjusted benchmarks. ML-UMR is an adaptation of
the ML-NMR methodology (Phillippo et al. 2020, <doi:10.1111/rssa.12579>)
implemented in the 'multinma' package (GPL-3) to the unanchored two-trial
case; the public API deliberately mirrors multinma's so users can move
between ML-NMR and ML-UMR with the same workflow.

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
