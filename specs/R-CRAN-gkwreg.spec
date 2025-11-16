%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gkwreg
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Kumaraswamy Regression Models for Bounded Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-gkwdist 
Requires:         R-CRAN-Formula 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-gkwdist 

%description
Implements regression models for bounded continuous data in the open
interval (0,1) using the five-parameter Generalized Kumaraswamy
distribution. Supports modeling all distribution parameters (alpha, beta,
gamma, delta, lambda) as functions of predictors through various link
functions. Provides efficient maximum likelihood estimation via Template
Model Builder ('TMB'), offering comprehensive diagnostics, model
comparison tools, and simulation methods. Particularly useful for
analyzing proportions, rates, indices, and other bounded response data
with complex distributional features not adequately captured by simpler
models.

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
