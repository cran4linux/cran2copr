%global packname  wallace
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Modular Platform for Reproducible Modeling of Species Niches and Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.2
BuildRequires:    R-CRAN-ENMeval >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-spocc >= 0.8.0
BuildRequires:    R-CRAN-DT >= 0.4
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spThin 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-leaflet >= 2.0.2
Requires:         R-CRAN-ENMeval >= 2.0.0
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-spocc >= 0.8.0
Requires:         R-CRAN-DT >= 0.4
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spThin 
Requires:         R-CRAN-zip 

%description
The 'shiny' application 'wallace' is a modular platform for reproducible
modeling of species niches and distributions. 'wallace' guides users
through a complete analysis, from the acquisition of species occurrence
and environmental data to visualizing model predictions on an interactive
map, thus bundling complex workflows into a single, streamlined interface.

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
