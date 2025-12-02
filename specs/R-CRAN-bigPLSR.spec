%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigPLSR
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Least Squares Regression Models with Big Matrices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-bigmemory 

%description
Fast partial least squares (PLS) for dense and out-of-core data. Provides
SIMPLS (straightforward implementation of a statistically inspired
modification of the PLS method) and NIPALS (non-linear iterative partial
least-squares) solvers, plus kernel-style PLS variants ('kernelpls' and
'widekernelpls') with parity to 'pls'. Optimized for 'bigmemory'-backed
matrices with streamed cross-products and chunked BLAS (Basic Linear
Algebra Subprograms) (XtX/XtY and XXt/YX), optional file-backed score
sinks, and deterministic testing helpers. Includes an auto-selection
strategy that chooses between XtX SIMPLS, XXt (wide) SIMPLS, and NIPALS
based on (n, p) and a configurable memory budget. About the package,
Bertrand and Maumy (2023) <https://hal.science/hal-05352069>, and
<https://hal.science/hal-05352061> highlighted fitting and
cross-validating PLS regression models to big data. For more details about
some of the techniques featured in the package, Dayal and MacGregor (1997)
<doi:10.1002/(SICI)1099-128X(199701)11:1%%3C73::AID-CEM435%%3E3.0.CO;2-%%23>,
Rosipal & Trejo (2001) <https://www.jmlr.org/papers/v2/rosipal01a.html>,
Tenenhaus, Viennet, and Saporta (2007) <doi:10.1016/j.csda.2007.01.004>,
Rosipal (2004) <doi:10.1007/978-3-540-45167-9_17>, Rosipal (2019)
<https://ieeexplore.ieee.org/document/8616346>, Song, Wang, and Bai (2024)
<doi:10.1016/j.chemolab.2024.105238>. Includes kernel logistic PLS with
'C++'-accelerated alternating iteratively reweighted least squares (IRLS)
updates, streamed reproducing kernel Hilbert space (RKHS) solvers with
reusable centering statistics, and bootstrap diagnostics with graphical
summaries for coefficients, scores, and cross-validation workflows,
alongside dedicated plotting utilities for individuals, variables,
ellipses, and biplots. The streaming backend uses far less memory and
keeps memory bounded across data sizes. For PLS1, streaming is often fast
enough while preserving a small memory footprint; for PLS2 it remains
competitive with a bounded footprint. On small problems that fit
comfortably in RAM (random-access memory), dense in-memory solvers are
slightly faster; the crossover occurs as n or p grow and the
Gram/cross-product cost dominates.

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
