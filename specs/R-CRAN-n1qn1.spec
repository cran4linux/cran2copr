%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  n1qn1
%global packver   6.0.1-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.1.12
Release:          1%{?dist}%{?buildtag}
Summary:          Port of the 'Scilab' 'n1qn1' Module for Unconstrained BFGS Optimization

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.5.600.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-Rcpp >= 0.12.3

%description
Provides 'Scilab' 'n1qn1'. This takes more memory than traditional L-BFGS.
The n1qn1 routine is useful since it allows prespecification of a Hessian.
If the Hessian is near enough the truth in optimization it can speed up
the optimization problem. The algorithm is described in the 'Scilab'
optimization documentation located at
<https://www.scilab.org/sites/default/files/optimization_in_scilab.pdf>.
This version uses manually modified code from 'f2c' to make this a C only
binary.

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
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
