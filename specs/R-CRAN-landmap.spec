%global packname  landmap
%global packver   0.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Spatial Prediction using Ensemble Machine Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-forestError 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-parallelMap 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-raster 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-forestError 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-parallelMap 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-raster 

%description
Functions and tools for spatial interpolation and/or prediction of
environmental variables (points to grids) based on using Ensemble Machine
Learning with geographical distances. Package also provides access to
Global Environmental Layers (<https://www.OpenLandMap.org>) produced by
the OpenGeoHub.org foundation and collaborators. Some functions have been
migrated and adopted from the Global Soil Information Facilities package.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
