%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  polykde
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Polyspherical Kernel Density Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-movMF 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-rotasym 
BuildRequires:    R-CRAN-sphunif 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.8.3
Requires:         R-CRAN-abind 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-movMF 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-rotasym 
Requires:         R-CRAN-sphunif 

%description
Kernel density estimation on the polysphere, (hyper)sphere, and circle.
Includes functions for density estimation, regression estimation, ridge
estimation, bandwidth selection, kernels, samplers, and homogeneity tests.
Companion package to García-Portugués and Meilán-Vila (2024)
<doi:10.48550/arXiv.2411.04166> and García-Portugués and Meilán-Vila
(2023) <doi:10.1007/978-3-031-32729-2_4>.

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
