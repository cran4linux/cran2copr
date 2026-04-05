%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CVXR
%global packver   1.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Disciplined Convex Optimization

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-cli >= 3.6
BuildRequires:    R-CRAN-scs >= 3.2
BuildRequires:    R-CRAN-Matrix >= 1.7
BuildRequires:    R-CRAN-highs >= 1.12
BuildRequires:    R-CRAN-Rcpp >= 1.1
BuildRequires:    R-CRAN-osqp >= 1.0
BuildRequires:    R-CRAN-gmp >= 0.7
BuildRequires:    R-CRAN-S7 >= 0.2
BuildRequires:    R-CRAN-clarabel >= 0.11
BuildRequires:    R-CRAN-slam >= 0.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-cli >= 3.6
Requires:         R-CRAN-scs >= 3.2
Requires:         R-CRAN-Matrix >= 1.7
Requires:         R-CRAN-highs >= 1.12
Requires:         R-CRAN-Rcpp >= 1.1
Requires:         R-CRAN-osqp >= 1.0
Requires:         R-CRAN-gmp >= 0.7
Requires:         R-CRAN-S7 >= 0.2
Requires:         R-CRAN-clarabel >= 0.11
Requires:         R-CRAN-slam >= 0.1
Requires:         R-methods 

%description
An object-oriented modeling language for disciplined convex programming
(DCP) as described in Fu, Narasimhan, and Boyd (2020,
<doi:10.18637/jss.v094.i14>). It allows the user to formulate convex
optimization problems in a natural way following mathematical convention
and DCP rules. The system analyzes the problem, verifies its convexity,
converts it into a canonical form, and hands it off to an appropriate
solver to obtain the solution. This version uses the S7 object system for
improved performance and maintainability.

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
