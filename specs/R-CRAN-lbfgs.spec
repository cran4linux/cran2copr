%global __brp_check_rpaths %{nil}
%global packname  lbfgs
%global packver   1.2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Limited-memory BFGS Optimization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-methods 

%description
A wrapper built around the libLBFGS optimization library by Naoaki
Okazaki. The lbfgs package implements both the Limited-memory
Broyden-Fletcher-Goldfarb-Shanno (L-BFGS) and the Orthant-Wise
Quasi-Newton Limited-Memory (OWL-QN) optimization algorithms. The L-BFGS
algorithm solves the problem of minimizing an objective, given its
gradient, by iteratively computing approximations of the inverse Hessian
matrix. The OWL-QN algorithm finds the optimum of an objective plus the
L1-norm of the problem's parameters. The package offers a fast and
memory-efficient implementation of these optimization routines, which is
particularly suited for high-dimensional problems.

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
