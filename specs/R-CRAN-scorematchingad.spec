%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scorematchingad
%global packver   0.0.60
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.60
Release:          1%{?dist}%{?buildtag}
Summary:          Score Matching Estimation by Automatic Differentiation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.7
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-FixedPoint 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ellipsis 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-FixedPoint 
Requires:         R-CRAN-Rdpack 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-R6 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ellipsis 

%description
Hyvärinen's score matching (Hyvärinen, 2005)
<https://jmlr.org/papers/v6/hyvarinen05a.html> is a useful estimation
technique when the normalising constant for a probability distribution is
difficult to compute. This package implements score matching estimators
using automatic differentiation in the 'CppAD' library
<https://github.com/coin-or/CppAD> and is designed for quickly
implementing score matching estimators for new models. Also available is
general robustification (Windham, 1995)
<https://www.jstor.org/stable/2346159>. Already in the package are
estimators for directional distributions (Mardia, Kent and Laha, 2016)
<doi:10.48550/arXiv.1604.08470> and the flexible Polynomially-Tilted
Pairwise Interaction model for compositional data. The latter estimators
perform well when there are zeros in the compositions (Scealy and Wood,
2023) <doi:10.1080/01621459.2021.2016422>, even many zeros (Scealy,
Hingee, Kent, and Wood, 2024) <doi:10.1007/s11222-024-10412-w>.

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
