%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ssdtools
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Species Sensitivity Distributions

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ssddata 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-universals 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-goftest 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-lifecycle 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ssddata 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-universals 
Requires:         R-utils 
Requires:         R-CRAN-VGAM 

%description
Species sensitivity distributions are cumulative probability distributions
which are fitted to toxicity concentrations for different species as
described by Posthuma et al.(2001) <isbn:9781566705783>.  The ssdtools
package uses Maximum Likelihood to fit distributions such as the gamma,
log-logistic, log-normal and Weibull to censored and/or weighted data.
Multiple distributions can be averaged using Akaike Information Criteria.
Confidence intervals on hazard concentrations and proportions are produced
by parametric bootstrapping.

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
