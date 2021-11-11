%global __brp_check_rpaths %{nil}
%global packname  CVXR
%global packver   1.0-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Disciplined Convex Optimization

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-scs >= 3.0
BuildRequires:    R-CRAN-ECOSolveR >= 0.5.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-scs >= 3.0
Requires:         R-CRAN-ECOSolveR >= 0.5.4
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-Rmpfr 
Requires:         R-stats 
Requires:         R-CRAN-osqp 

%description
An object-oriented modeling language for disciplined convex programming
(DCP) as described in Fu, Narasimhan, and Boyd (2020,
<doi:10.18637/jss.v094.i14>). It allows the user to formulate convex
optimization problems in a natural way following mathematical convention
and DCP rules. The system analyzes the problem, verifies its convexity,
converts it into a canonical form, and hands it off to an appropriate
solver to obtain the solution. Interfaces to solvers on CRAN and elsewhere
are provided, both commercial and open source.

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
