%global __brp_check_rpaths %{nil}
%global packname  rsat
%global packver   0.1.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.18
Release:          1%{?dist}%{?buildtag}
Summary:          Dealing with Multiplatform Satellite Images

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-leafem 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-tmap 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-calendR 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-leafem 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-tmap 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-zip 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-calendR 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-terra 

%description
Downloading, customizing, and processing time series of satellite images
for a region of interest. 'rsat' functions allow a unified access to
multispectral images from Landsat, MODIS and Sentinel repositories. 'rsat'
also offers capabilities for customizing satellite images, such as tile
mosaicking, image cropping and new variables computation. Finally, 'rsat'
covers the processing, including cloud masking, compositing and
gap-filling/smoothing time series of images (Militino et al., 2018
<doi:10.3390/rs10030398> and Militino et al., 2019
<doi:10.1109/TGRS.2019.2904193>).

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
