%global __brp_check_rpaths %{nil}
%global packname  Qtools
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Quantiles

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glmx 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-numDeriv >= 2016.8.1
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-utils 
Requires:         R-CRAN-glmx 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-np 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-boot 

%description
Functions for unconditional and conditional quantiles. These include
methods for transformation-based quantile regression, quantile-based
measures of location, scale and shape, methods for quantiles of discrete
variables, quantile-based multiple imputation, restricted quantile
regression, and directional quantile classification. A vignette is given
in Geraci (2016, The R Journal) <doi:10.32614/RJ-2016-037> and included in
the package.

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
