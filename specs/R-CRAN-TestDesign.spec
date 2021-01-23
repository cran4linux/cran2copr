%global packname  TestDesign
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Test Design Approach to Fixed and Adaptive Test Construction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-logitnorm 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-logitnorm 
Requires:         R-CRAN-crayon 

%description
Use the optimal test design approach by Birnbaum (1968,
ISBN:9781593119348) and van der Linden (2018) <doi:10.1201/9781315117430>
in constructing fixed and adaptive tests. Supports the following
mixed-integer programming (MIP) solver packages: 'lpsymphony',
'Rsymphony', 'gurobi', 'lpSolve', and 'Rglpk'. The 'gurobi' package is not
available from CRAN; see <https://www.gurobi.com/downloads/>. See vignette
for installing 'Rsymphony' package on Mac systems.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
