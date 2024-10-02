%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gbp
%global packver   0.1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Bin Packing Problem Solver

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-rgl 

%description
Basic infrastructure and several algorithms for 1d-4d bin packing problem.
This package provides a set of c-level classes and solvers for 1d-4d bin
packing problem, and an r-level solver for 4d bin packing problem, which
is a wrapper over the c-level 4d bin packing problem solver. The 4d bin
packing problem solver aims to solve bin packing problem, a.k.a container
loading problem, with an additional constraint on weight. Given a set of
rectangular-shaped items, and a set of rectangular-shaped bins with weight
limit, the solver looks for an orthogonal packing solution such that
minimizes the number of bins and maximize volume utilization. Each
rectangular-shaped item i = 1, .. , n is characterized by length l_i,
depth d_i, height h_i, and weight w_i, and each rectangular-shaped bin j =
1, .. , m is specified similarly by length l_j, depth d_j, height h_j, and
weight limit w_j. The item can be rotated into any orthogonal direction,
and no further restrictions implied.

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
