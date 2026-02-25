%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survey
%global packver   4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Complex Survey Samples

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-mitools >= 2.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mitools >= 2.4
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-splines 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-numDeriv 

%description
Summary statistics, two-sample tests, rank tests, generalised linear
models, cumulative link models, Cox models, loglinear models, and general
maximum pseudolikelihood estimation for multistage stratified,
cluster-sampled, unequally weighted survey samples. Variances by Taylor
series linearisation or replicate weights. Post-stratification,
calibration, and raking. Two-phase and multiphase subsampling designs.
Graphics. PPS sampling without replacement. Small-area estimation.
Dual-frame designs.

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
