%global __brp_check_rpaths %{nil}
%global packname  agroclim
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Climatic Indices for Agriculture

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-easyNCDF 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-multiApply 
BuildRequires:    R-tools 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-easyNCDF 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-multiApply 
Requires:         R-tools 

%description
Collection of functions to compute agroclimatic indices useful to zoning
areas based on climatic variables and to evaluate the importance of
temperature and precipitation for individual crops, or in general for
agricultural lands.

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
