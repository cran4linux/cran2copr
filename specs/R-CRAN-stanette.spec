%global __brp_check_rpaths %{nil}
%global packname  stanette
%global packver   2.21.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.21.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-loo >= 2.3.0
BuildRequires:    R-CRAN-StanHeaders >= 2.21.0
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-BH >= 1.72.0.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-loo >= 2.3.0
Requires:         R-CRAN-StanHeaders >= 2.21.0
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-lattice 
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-CRAN-inline 
Requires:         R-CRAN-pkgbuild 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-brew 
Requires:         R-CRAN-coda 

%description
Expansion and additions to 'rstan' to facilitate pharmacokinetics (PK) and
pharmacodynamics (PD) modeling with 'rstan'.  A PKPD model often is
specified via a set of ordinary differential equations(ODEs) and requires
flexible and different routes of drug administrations.  These features
make PKPD modeling with plain 'rstan' challenging and tedious to code.
'stanette' provides a powerful Stan-compatible ODE solver ('LSODA') and
mechanism/utilities that make easy specification of flexible dosing
records.

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
