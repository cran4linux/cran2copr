%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  piqp
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to Proximal Interior Point Quadratic Programming Solver

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-S7 

%description
An embedded proximal interior point quadratic programming solver, which
can solve dense and sparse quadratic programs, described in Schwan, Jiang,
Kuhn, and Jones (2023) <doi:10.48550/arXiv.2304.00290>. Combining an
infeasible interior point method with the proximal method of multipliers,
the algorithm can handle ill-conditioned convex quadratic programming
problems without the need for linear independence of the constraints. The
solver is written in header only 'C++ 14' leveraging the 'Eigen' library
for vectorized linear algebra. For small dense problems, vectorized
instructions and cache locality can be exploited more efficiently.
Allocation free problem updates and re-solves are also provided.

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
