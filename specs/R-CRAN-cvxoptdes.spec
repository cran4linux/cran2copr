%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cvxoptdes
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Convex Optimal Experiment Design

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-mirai 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-reformulas 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-mirai 

%description
Convex optimal experiment design across discrete candidate grids using
open-source optimization solvers. Specifies and optimizes designs using an
object-oriented interface (via 'R6') for linear models, generalized
linear/additive models, nonlinear models, and random intercept linear
mixed models. Optimization and augmentation of weighted, penalized and
convex constrained approximate designs is supported using the Splitting
Cone Solver (SCS). Optimal rounding to integer-valued designs is supported
using point-exchange methods or mixed-integer programming with the 'HiGHS'
solver. For details, see Chau et al. (2026)
<doi:10.48550/arXiv.2610.14288>.

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
