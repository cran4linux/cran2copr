%global packname  plotKML
%global packver   0.8-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of Spatial and Spatio-Temporal Objects in Google Earth

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-landmap 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-aqp 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-pixmap 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RSAGA 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-landmap 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-aqp 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-pixmap 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-RSAGA 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 

%description
Writes sp-class, spacetime-class, raster-class and similar spatial and
spatio-temporal objects to KML following some basic cartographic rules.

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
