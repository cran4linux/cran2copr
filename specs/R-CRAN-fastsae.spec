%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastsae
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Implementation of Small Area Estimation Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides high-performance implementations of Small Area Estimation (SAE)
methods leveraging C++ ('Rcpp', 'RcppArmadillo') and 'OpenMP'
multi-threading. Supports standard area-level Fay-Herriot models (Fay and
Herriot, 1979 <doi:10.1080/01621459.1979.10482505>), Spatial Fay-Herriot
models (Pratesi and Salvati, 2008 <doi:10.1002/env.861>), Spatio-Temporal
Fay-Herriot models (Marhuenda et al., 2013
<doi:10.1016/j.csda.2013.01.016>), and unit-level Battese-Harter-Fuller
models (Battese et al., 1988 <doi:10.1080/01621459.1988.10478561>).
Features include empirical best linear unbiased prediction (EBLUP),
analytical and bootstrap Mean Squared Error (MSE) estimation, automatic
handling of unsampled domains, and modern S3 diagnostic methods.

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
