%global __brp_check_rpaths %{nil}
%global packname  FME
%global packver   1.3.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Flexible Modelling Environment for Inverse Modelling, Sensitivity, Identifiability and Monte Carlo Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6
Requires:         R-core >= 2.6
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-minqa 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-minqa 

%description
Provides functions to help in fitting models to data, to perform Monte
Carlo, sensitivity and identifiability analysis. It is intended to work
with models be written as a set of differential equations that are solved
either by an integration routine from package 'deSolve', or a steady-state
solver from package 'rootSolve'. However, the methods can also be used
with other types of functions.

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
