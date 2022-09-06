%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spmoran
%global packver   0.2.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Spatial Regression using Moran Eigenvectors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
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
Requires:         R-CRAN-sp 
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
Functions for estimating spatial varying coefficient models, mixed models,
and other spatial regression models for Gaussian and non-Gaussian data.
Moran eigenvectors are used to an approximate Gaussian process modeling
which is interpretable in terms of the Moran coefficient. The GP is used
for modeling the spatial processes in residuals and regression
coefficients. For details see Murakami (2021) <arXiv:1703.04467>.

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
