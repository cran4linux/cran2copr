%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pnd
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Numerical Derivatives, Gradients, Jacobians, and Hessians of Arbitrary Accuracy Order

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-parallel 
Requires:         R-CRAN-Rdpack 

%description
Calculation of numerical derivatives through finite-difference
approximations with parallel capabilities and optimal step-size selection
to improve accuracy. These functions facilitate efficient computation of
derivatives, gradients, Jacobians, and Hessians, allowing for more
evaluations to reduce the mathematical and machine errors. Designed for
compatibility with the 'numDeriv' package, which has not received updates
in several years, it introduces advanced features such as computing
derivatives of arbitrary order, improving the accuracy of Hessian
approximations by avoiding repeated differencing, and parallelising slow
functions on Windows, Mac, and Linux.

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
