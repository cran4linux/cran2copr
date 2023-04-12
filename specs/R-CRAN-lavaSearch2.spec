%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lavaSearch2
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Model Specification in the Latent Variable Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-lava >= 1.6.4
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-lava >= 1.6.4
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for model specification in the latent variable framework (add-on to
the 'lava' package). The package contains three main functionalities: Wald
tests/F-tests with improved control of the type 1 error in small samples,
adjustment for multiple comparisons when searching for local dependencies,
and adjustment for multiple comparisons when doing inference for multiple
latent variable models.

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
