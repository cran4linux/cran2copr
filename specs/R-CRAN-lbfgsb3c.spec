%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lbfgsb3c
%global packver   2024-3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2024.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Limited Memory BFGS Minimizer with Bounds on Parameters with optim() 'C' Interface

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-numDeriv 
Requires:         R-methods 

%description
Interfacing to Nocedal et al. L-BFGS-B.3.0 (See
<http://users.iems.northwestern.edu/~nocedal/lbfgsb.html>) limited memory
BFGS minimizer with bounds on parameters. This is a fork of 'lbfgsb3'.
This registers a 'R' compatible 'C' interface to L-BFGS-B.3.0 that uses
the same function types and optimization as the optim() function (see
writing 'R' extensions and source for details).  This package also adds
more stopping criteria as well as allowing the adjustment of more
tolerances.

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
