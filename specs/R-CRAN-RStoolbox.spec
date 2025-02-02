%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RStoolbox
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Remote Sensing Data Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-caret >= 6.0.79
BuildRequires:    R-CRAN-terra >= 1.6.41
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-exactextractr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-caret >= 6.0.79
Requires:         R-CRAN-terra >= 1.6.41
Requires:         R-CRAN-sf 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-exactextractr 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 

%description
Toolbox for remote sensing image processing and analysis such as
calculating spectral indexes, principal component transformation,
unsupervised and supervised classification or fractional cover analyses.

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
