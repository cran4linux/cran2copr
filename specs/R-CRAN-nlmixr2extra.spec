%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlmixr2extra
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Mixed Effects Models in Population PK/PD, Extra Support Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-nlmixr2est >= 2.1.1
BuildRequires:    R-CRAN-rxode2 >= 2.0.10
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lotri 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-symengine 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-nlmixr2est >= 2.1.1
Requires:         R-CRAN-rxode2 >= 2.0.10
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lotri 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-symengine 
Requires:         R-utils 

%description
Fit and compare nonlinear mixed-effects models in differential equations
with flexible dosing information commonly seen in pharmacokinetics and
pharmacodynamics (Almquist, Leander, and Jirstrand 2015
<doi:10.1007/s10928-015-9409-1>). Differential equation solving is by
compiled C code provided in the 'rxode2' package (Wang, Hallow, and James
2015 <doi:10.1002/psp4.12052>). This package is for support functions like
preconditioned fits <doi:10.1208/s12248-016-9866-5>, boostrap and stepwise
covariate selection.

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
