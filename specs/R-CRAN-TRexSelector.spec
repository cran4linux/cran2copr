%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TRexSelector
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          T-Rex Selector: High-Dimensional Variable Selection and FDR Control

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-Rcereal 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 

%description
Variable selection for regression and classification in high-dimensional
settings with control of the false discovery rate (FDR) at a
user-specified target level. The implementations are primarily based on
the T-Rex selector of Machkour, Muma and Palomar (2025)
<doi:10.1016/j.sigpro.2025.109894> and its dependency-aware extension for
correlated variables by Machkour, Muma and Palomar (2025)
<doi:10.1016/j.sigpro.2025.109990>. Since version 2.0.0 the package comes
as R bindings to the 'TRexSelector' C++ library, which replaces the pure-R
implementation of the 1.x releases.

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
