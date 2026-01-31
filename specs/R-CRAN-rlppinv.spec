%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rlppinv
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Programming via Regularized Least Squares

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rclsp >= 0.3.0
Requires:         R-CRAN-rclsp >= 0.3.0

%description
The Linear Programming via Regularized Least Squares (LPPinv) is a
two-stage estimation method that reformulates linear programs as
structured least-squares problems. Based on the Convex Least Squares
Programming (CLSP) framework, LPPinv solves linear inequality, equality,
and bound constraints by (1) constructing a canonical constraint system
and computing a pseudoinverse projection, followed by (2) a
convex-programming correction stage to refine the solution under
additional regularization (e.g., Lasso, Ridge, or Elastic Net). LPPinv is
intended for underdetermined and ill-posed linear problems, for which
standard solvers fail.

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
