%global packname  MtreeRing
%global packver   1.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          A Shiny Application for Automatic Measurements of Tree-Ring Widths on Digital Images

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-bmp 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-dplR 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-measuRing 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-bmp 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-dplR 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-measuRing 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyWidgets 

%description
Use morphological image processing and edge detection algorithms to
automatically measure tree ring widths on digital images. Users can also
manually mark tree rings on species with complex anatomical structures.
The arcs of inner-rings and angles of successive inclined ring boundaries
are used to correct ring-width series. The package provides a Shiny-based
application, allowing R beginners to easily analyze tree ring images and
export ring-width series in standard file formats.

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
