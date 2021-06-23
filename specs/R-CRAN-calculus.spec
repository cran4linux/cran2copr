%global __brp_check_rpaths %{nil}
%global packname  calculus
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Numerical and Symbolic Calculus

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
Efficient C++ optimized functions for numerical and symbolic calculus as
described in Guidotti (2020) <arXiv:2101.00086>. It includes basic
arithmetic, tensor calculus, Einstein summing convention, fast computation
of the Levi-Civita symbol and generalized Kronecker delta, Taylor series
expansion, multivariate Hermite polynomials, high-order derivatives,
ordinary differential equations, differential operators (Gradient,
Jacobian, Hessian, Divergence, Curl, Laplacian) and numerical integration
in arbitrary orthogonal coordinate systems: cartesian, polar, spherical,
cylindrical, parabolic or user defined by custom scale factors.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
