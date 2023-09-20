%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sctransform
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variance Stabilizing Transformations for Single Cell UMI Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-matrixStats 

%description
A normalization method for single-cell UMI count data using a variance
stabilizing transformation. The transformation is based on a negative
binomial regression model with regularized parameters. As part of the same
regression framework, this package also provides functions for batch
correction, and data correction. See Hafemeister and Satija (2019)
<doi:10.1186/s13059-019-1874-1>, and Choudhary and Satija (2022)
<doi:10.1186/s13059-021-02584-9> for more details.

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
