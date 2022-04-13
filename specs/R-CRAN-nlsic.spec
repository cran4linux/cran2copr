%global __brp_check_rpaths %{nil}
%global packname  nlsic
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Non Linear Least Squares with Inequality Constraints

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nnls 
Requires:         R-CRAN-nnls 

%description
We solve non linear least squares problems with optional equality and/or
inequality constraints. Non linear iterations are globalized with
back-tracking method. Linear problems are solved by dense QR decomposition
from 'LAPACK' which can limit the size of treated problems. On the other
side, we avoid condition number degradation which happens in classical
quadratic programming approach. Inequality constraints treatment on each
non linear iteration is based on 'NNLS' method (by Lawson and Hanson). We
provide an original function 'lsi_ln' for solving linear least squares
problem with inequality constraints in least norm sens. Thus if Jacobian
of the problem is rank deficient a solution still can be provided.
However, truncation errors are probable in this case. Equality constraints
are treated by using a basis of Null-space. User defined function
calculating residuals must return a list having residual vector (not their
squared sum) and Jacobian. If Jacobian is not in the returned list,
package 'numDeriv' is used to calculated finite difference version of
Jacobian. The 'NLSIC' method was fist published in Sokol et al. (2012)
<doi:10.1093/bioinformatics/btr716>.

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
