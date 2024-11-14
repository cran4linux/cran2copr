%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mclustAddons
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Addons for the 'mclust' Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-mclust >= 6.1
BuildRequires:    R-CRAN-doRNG >= 1.6
BuildRequires:    R-CRAN-knitr >= 1.12
BuildRequires:    R-CRAN-Rcpp >= 1.0
BuildRequires:    R-CRAN-rmarkdown >= 0.9
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-mclust >= 6.1
Requires:         R-CRAN-doRNG >= 1.6
Requires:         R-CRAN-knitr >= 1.12
Requires:         R-CRAN-Rcpp >= 1.0
Requires:         R-CRAN-rmarkdown >= 0.9
Requires:         R-CRAN-cli 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Extend the functionality of the 'mclust' package for Gaussian finite
mixture modeling by including: density estimation for data with bounded
support (Scrucca, 2019 <doi:10.1002/bimj.201800174>); modal clustering
using MEM (Modal EM) algorithm for Gaussian mixtures (Scrucca, 2021
<doi:10.1002/sam.11527>); entropy estimation via Gaussian mixture modeling
(Robin & Scrucca, 2023 <doi:10.1016/j.csda.2022.107582>); Gaussian
mixtures modeling of financial log-returns (Scrucca, 2024
<doi:10.3390/e26110907>).

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
