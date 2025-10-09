%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CMLS
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Multivariate Least Squares

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-parallel 
Requires:         R-CRAN-quadprog 
Requires:         R-parallel 

%description
Solves multivariate least squares (MLS) problems subject to constraints on
the coefficients, e.g., non-negativity, orthogonality, equality,
inequality, monotonicity, unimodality, smoothness, etc. Includes flexible
functions for solving MLS problems subject to user-specified equality
and/or inequality constraints, as well as a wrapper function that
implements 24 common constraint options. Also does k-fold or generalized
cross-validation to tune constraint options for MLS problems. See ten
Berge (1993, ISBN:9789066950832) for an overview of MLS problems, and see
Goldfarb and Idnani (1983) <doi:10.1007/BF02591962> for a discussion of
the underlying quadratic programming algorithm.

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
