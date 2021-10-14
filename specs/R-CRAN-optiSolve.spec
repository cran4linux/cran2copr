%global __brp_check_rpaths %{nil}
%global packname  optiSolve
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linear, Quadratic, and Rational Optimization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-cccp 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-shapes 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-cccp 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 
Requires:         R-stats 

%description
Solver for linear, quadratic, and rational programs with linear,
quadratic, and rational constraints. A unified interface to different R
packages is provided. Optimization problems are transformed into
equivalent formulations and solved by the respective package. For example,
quadratic programming problems with linear, quadratic and rational
constraints can be solved by augmented Lagrangian minimization using
package 'alabama', or by sequential quadratic programming using solver
'slsqp'.  Alternatively, they can be reformulated as optimization problems
with second order cone constraints and solved with package 'cccp'.

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
