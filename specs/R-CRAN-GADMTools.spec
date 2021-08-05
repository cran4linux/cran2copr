%global __brp_check_rpaths %{nil}
%global packname  GADMTools
%global packver   3.9-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Use of 'GADM' Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rosm 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-ggspatial 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-prettymapr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rgdal 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rosm 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-ggspatial 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-prettymapr 

%description
Manipulate, assemble, export <https://gadm.org/> maps. Create
'choropleth', 'isopleth', dots plot, proportional dots, dot-density and
more.

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
