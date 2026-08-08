%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatialkit
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Tessellation, Modeling, and Cross-Validation Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-sf >= 1.0
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-logger 
Requires:         R-CRAN-digest 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-parallel 

%description
A modular toolkit for spatial analysis workflows including coordinate
reference system management, Voronoi/Delaunay/grid tessellation,
feature-to-polygon assignment, geographically weighted regression (GWR,
via 'GWmodel'), Bayesian spatial Gaussian process regression (via 'brms'),
spatial cross-validation with block and buffered strategies, and model
comparison. Provides an S3 class system ('spatial_fit') with consistent
predict, fitted, and residuals methods across model backends.

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
