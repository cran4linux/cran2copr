%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  circlus
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering and Simulation of Spherical Cauchy and PKBD Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Tinflex >= 1.8
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Tinflex >= 1.8
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-torch 
Requires:         R-methods 

%description
Provides tools for estimation and clustering of spherical data, seamlessly
integrated with the 'flexmix' package. Includes the necessary M-step
implementations for both Poisson Kernel-Based Distribution (PKBD) and
spherical Cauchy distribution. Additionally, the package provides random
number generators for PKBD and spherical Cauchy distribution. Methods are
based on Golzy M., Markatou M. (2020) <doi:10.1080/10618600.2020.1740713>,
Kato S., McCullagh P. (2020) <doi:10.3150/20-bej1222> and Sablica L.,
Hornik K., Leydold J. (2023) <doi:10.1214/23-ejs2149>.

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
