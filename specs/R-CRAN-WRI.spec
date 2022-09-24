%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WRI
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Wasserstein Regression and Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-modeest >= 2.4.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-Rfast >= 1.9.8
BuildRequires:    R-CRAN-locfit >= 1.5.9.1
BuildRequires:    R-CRAN-mvtnorm >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-expm >= 0.999.4
BuildRequires:    R-CRAN-CVXR >= 0.99.7
BuildRequires:    R-CRAN-locpol >= 0.7
BuildRequires:    R-CRAN-fdapace >= 0.2.0
BuildRequires:    R-CRAN-fdadensity >= 0.1.2
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-modeest >= 2.4.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-Rfast >= 1.9.8
Requires:         R-CRAN-locfit >= 1.5.9.1
Requires:         R-CRAN-mvtnorm >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-expm >= 0.999.4
Requires:         R-CRAN-CVXR >= 0.99.7
Requires:         R-CRAN-locpol >= 0.7
Requires:         R-CRAN-fdapace >= 0.2.0
Requires:         R-CRAN-fdadensity >= 0.1.2
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-polynom 

%description
Implementation of the methodologies described in 1) Alexander Petersen, Xi
Liu and Afshin A. Divani (2021) <doi:10.1214/20-aos1971>, including global
F tests, partial F tests, intrinsic Wasserstein-infinity bands and
Wasserstein density bands, and 2) Chao Zhang, Piotr Kokoszka and Alexander
Petersen (2022) <doi:10.1111/jtsa.12590>, including estimation,
prediction, and inference of the Wasserstein autoregressive models.

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
