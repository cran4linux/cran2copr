%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  enmSdmX
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Species Distribution Modeling and Ecological Niche Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AICcmodavg 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-maxnet 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-omnibus 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-predicts 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-statisfactory 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-AICcmodavg 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gbm 
Requires:         R-graphics 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-maxnet 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-omnibus 
Requires:         R-parallel 
Requires:         R-CRAN-predicts 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-statisfactory 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
Implements species distribution modeling and ecological niche modeling,
including: bias correction, spatial cross-validation, model evaluation,
raster interpolation, biotic "velocity" (speed and direction of movement
of a "mass" represented by a raster), interpolating across a time series
of rasters, and use of spatially imprecise records. The heart of the
package is a set of "training" functions which automatically optimize
model complexity based number of available occurrences. These algorithms
include MaxEnt, MaxNet, boosted regression trees/gradient boosting
machines, generalized additive models, generalized linear models, natural
splines, and random forests. To enhance interoperability with other
modeling packages, no new classes are created. The package works with
'PROJ6' geodetic objects and coordinate reference systems.

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
