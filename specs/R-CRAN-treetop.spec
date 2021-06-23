%global __brp_check_rpaths %{nil}
%global packname  treetop
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Shiny-Based Application for Extracting Forest Information from LiDAR Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.core 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-rglwidget 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.core 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rasterVis 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-lidR 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-rglwidget 

%description
Set of tools implemented into a shiny-based application for extracting and
analyzing individual tree forest attributes from LiDAR (Light Detection
and Ranging) data.

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
