%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rxode2
%global packver   2.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Facilities for Simulating from ODE-Based Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-rxode2ll >= 2.0.9
BuildRequires:    R-CRAN-rxode2et >= 2.0.9
BuildRequires:    R-CRAN-rxode2random >= 2.0.9
BuildRequires:    R-CRAN-rxode2parse >= 2.0.11
BuildRequires:    R-CRAN-cli >= 2.0.0
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.300.2.0
BuildRequires:    R-CRAN-lotri >= 0.4.0
BuildRequires:    R-CRAN-PreciseSums >= 0.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rex 
BuildRequires:    R-CRAN-sys 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-qs 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-rxode2ll >= 2.0.9
Requires:         R-CRAN-rxode2et >= 2.0.9
Requires:         R-CRAN-rxode2random >= 2.0.9
Requires:         R-CRAN-rxode2parse >= 2.0.11
Requires:         R-CRAN-cli >= 2.0.0
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-lotri >= 0.4.0
Requires:         R-CRAN-PreciseSums >= 0.3
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-backports 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-inline 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-rex 
Requires:         R-CRAN-sys 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-qs 

%description
Facilities for running simulations from ordinary differential equation
('ODE') models, such as pharmacometrics and other compartmental models.  A
compilation manager translates the ODE model into C, compiles it, and
dynamically loads the object code into R for improved computational
efficiency.  An event table object facilitates the specification of
complex dosing regimens (optional) and sampling schedules.  NB: The use of
this package requires both C and Fortran compilers, for details on their
use with R please see Section 6.3, Appendix A, and Appendix D in the "R
Administration and Installation" manual. Also the code is mostly released
under GPL.  The 'VODE' and 'LSODA' are in the public domain.  The
information is available in the inst/COPYRIGHTS.

%prep
%setup -q -c -n %{packname}
sed -i '/RcppEigen/,+12d' %{packname}/inst/tools/workaround.R
sed -i 's/-@ISYSTEM@"$(EG)" @SH@//' %{packname}/src/Makevars.in
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
