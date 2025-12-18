%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  intRinsic
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood-Based Intrinsic Dimension Estimators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-salso 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-salso 

%description
Provides functions to estimate the intrinsic dimension of a dataset via
likelihood-based approaches. Specifically, the package implements the
'TWO-NN' and 'Gride' estimators and the 'Hidalgo' Bayesian mixture model.
In addition, the first reference contains an extended vignette on the
usage of the 'TWO-NN' and 'Hidalgo' models. References: Denti (2023,
<doi:10.18637/jss.v106.i09>); Allegra et al. (2020,
<doi:10.1038/s41598-020-72222-0>); Denti et al. (2022,
<doi:10.1038/s41598-022-20991-1>); Facco et al. (2017,
<doi:10.1038/s41598-017-11873-y>); Santos-Fernandez et al. (2021,
<doi:10.1038/s41598-022-20991-1>).

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
