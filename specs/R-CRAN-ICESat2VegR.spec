%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ICESat2VegR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          ICESat-2 Data Analysis for Land and Vegetation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-geojsonsf 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-googleCloudStorageR 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-servr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-geojsonsf 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-googleCloudStorageR 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mathjaxr 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-servr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xml2 

%description
Provides tools for downloading, reading, processing, visualizing, and
exporting NASA's ICESat-2 ATL03 (Global Geolocated Photon Data) and ATL08
(Land and Vegetation Height) products. Supports photon- and segment-level
analysis, spatial sampling, gridding, statistical and machine-learning
modeling, and integration with 'Google Earth Engine'
(<https://earthengine.google.com/>) for wall-to-wall mapping of vegetation
structure and other land attributes.

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
