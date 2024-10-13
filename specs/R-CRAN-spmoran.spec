%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spmoran
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Spatial and Spatio-Temporal Regression using Moran Eigenvectors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-splines 
Requires:         R-CRAN-FNN 
Requires:         R-methods 

%description
A collection of functions for estimating spatial and spatio-temporal
regression models. Moran eigenvectors are used as spatial basis functions
to efficiently approximate spatially dependent Gaussian processes (i.e.,
random effects eigenvector spatial filtering; see Murakami and Griffith
2015 <doi: 10.1007/s10109-015-0213-7>). The implemented models include
linear regression with residual spatial dependence,
spatially/spatio-temporally varying coefficient models (Murakami et al.,
2017, 2024;
<doi:10.1016/j.spasta.2016.12.001>,<doi:10.48550/arXiv.2410.07229>),
spatially filtered unconditional quantile regression (Murakami and Seya,
2019 <doi:10.1002/env.2556>), Gaussian and non-Gaussian spatial mixed
models through compositionally-warping (Murakami et al. 2021,
<doi:10.1016/j.spasta.2021.100520>).

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
