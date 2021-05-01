%global packname  xROI
%global packver   0.9.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.19
Release:          1%{?dist}%{?buildtag}
Summary:          Delineate Region of Interests (ROI's) and Extract Time-Series Data from Digital Repeat Photography Images

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-data.table 
Requires:         R-graphics 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tiff 
Requires:         R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 

%description
Digital repeat photography and near-surface remote sensing have been used
by environmental scientists to study the environmental change for nearly a
decade. However, a user-friendly, reliable, and robust platform to extract
color-based statistics and time-series from a large stack of images is
still lacking. Here, we present an interactive open-source toolkit, called
'xROI', that facilitate the process time-series extraction and improve the
quality of the final data. 'xROI' provides a responsive environment for
scientists to interactively a) delineate regions of interest (ROI), b)
handle field of view (FOV) shifts, and c) extract and export time series
data characterizing image color (i.e. red, green and blue channel digital
numbers for the defined ROI). Using 'xROI', user can detect FOV shifts
without minimal difficulty. The software gives user the opportunity to
readjust the mask files or redraw new ones every time an FOV shift occurs.
'xROI' helps to significantly improve data accuracy and continuity.

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
