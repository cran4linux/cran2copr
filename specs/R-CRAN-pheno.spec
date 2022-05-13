%global __brp_check_rpaths %{nil}
%global packname  pheno
%global packver   1.7-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Auxiliary Functions for Phenological Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-quantreg 
Requires:         R-methods 
Requires:         R-stats 

%description
Provides some easy-to-use functions for time series analyses of (plant-)
phenological data sets. These functions mainly deal with the estimation of
combined phenological time series and are usually wrappers for functions
that are already implemented in other R packages adapted to the special
structure of phenological data and the needs of phenologists. Some date
conversion functions to handle Julian dates are also provided.

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
