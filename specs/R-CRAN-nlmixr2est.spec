%global __brp_check_rpaths %{nil}
%global packname  nlmixr2est
%global packver   2.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Mixed Effects Models in Population PK/PD, Estimation Routines

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-n1qn1 >= 6.0.1.10
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rxode2 >= 2.0.7
BuildRequires:    R-CRAN-RcppArmadillo >= 0.5.600.2.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-dparser >= 0.1.8
BuildRequires:    R-CRAN-nlmixr2data 
BuildRequires:    R-CRAN-lbfgsb3c 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rex 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-symengine 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-n1qn1 >= 6.0.1.10
Requires:         R-CRAN-rxode2 >= 2.0.7
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-nlmixr2data 
Requires:         R-CRAN-lbfgsb3c 
Requires:         R-CRAN-dparser >= 0.1.8
Requires:         R-methods 
Requires:         R-CRAN-rex 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-backports 
Requires:         R-CRAN-symengine 

%description
Fit and compare nonlinear mixed-effects models in differential equations
with flexible dosing information commonly seen in pharmacokinetics and
pharmacodynamics (Almquist, Leander, and Jirstrand 2015
<doi:10.1007/s10928-015-9409-1>). Differential equation solving is by
compiled C code provided in the 'rxode2' package (Wang, Hallow, and James
2015 <doi:10.1002/psp4.12052>).

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
