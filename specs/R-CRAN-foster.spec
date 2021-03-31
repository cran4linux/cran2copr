%global packname  foster
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Structure Extrapolation with R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RStoolbox 
BuildRequires:    R-CRAN-yaImpute 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-trend 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-raster 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-RStoolbox 
Requires:         R-CRAN-yaImpute 
Requires:         R-CRAN-sp 
Requires:         R-tools 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-trend 
Requires:         R-CRAN-data.table 

%description
Set of tools to streamline the modeling of the relationship between
satellite imagery time series or any other environmental information, such
as terrain elevation, with forest structural attributes derived from 3D
point cloud data and their subsequent imputation over the broader
landscape.

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
