%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatialEco
%global packver   2.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Analysis and Modelling Utilities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat.geom >= 3.0.3
BuildRequires:    R-CRAN-SpatialPack >= 0.3
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-yaImpute 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-spatstat.geom >= 3.0.3
Requires:         R-CRAN-SpatialPack >= 0.3
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-yaImpute 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-MASS 

%description
Utilities to support spatial data manipulation, query, sampling and
modelling in ecological applications. Functions include models for species
population density, spatial smoothing, multivariate separability, point
process model for creating pseudo- absences and sub-sampling,
Quadrant-based sampling and analysis, auto-logistic modeling, sampling
models, cluster optimization, statistical exploratory tools and
raster-based metrics.

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
