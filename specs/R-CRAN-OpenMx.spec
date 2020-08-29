%global packname  OpenMx
%global packver   2.18.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.18.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Structural Equation Modelling

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-StanHeaders >= 2.10.0.2
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-rpf >= 0.45
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-digest 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-CRAN-lifecycle 

%description
Create structural equation models that can be manipulated
programmatically. Models may be specified with matrices or paths (LISREL
or RAM) Example models include confirmatory factor, multiple group,
mixture distribution, categorical threshold, modern test theory,
differential Fit functions include full information maximum likelihood,
maximum likelihood, and weighted least squares. equations, state space,
and many others. Support and advanced package binaries available at
<http://openmx.ssri.psu.edu>. The software is described in Neale, Hunter,
Pritikin, Zahery, Brick, Kirkpatrick, Estabrook, Bates, Maes, & Boker
(2016) <doi:10.1007/s11336-014-9435-8>.

%prep
%setup -q -c -n %{packname}
find %{packname} -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \;
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
