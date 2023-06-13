%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MODIStsp
%global packver   2.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Find, Download and Process MODIS Land Products Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 3.3.13
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-bitops >= 1.0.6
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-xts >= 0.9.7
BuildRequires:    R-CRAN-sf >= 0.9.3
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-gdalUtilities 
BuildRequires:    R-CRAN-geojsonio 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-parallel 
Requires:         R-CRAN-raster >= 3.3.13
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-bitops >= 1.0.6
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-xts >= 0.9.7
Requires:         R-CRAN-sf >= 0.9.3
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-gdalUtilities 
Requires:         R-CRAN-geojsonio 
Requires:         R-CRAN-jsonlite 
Requires:         R-parallel 

%description
Allows automating the creation of time series of rasters derived from
MODIS satellite land products data. It performs several typical
preprocessing steps such as download, mosaicking, reprojecting and
resizing data acquired on a specified time period. All processing
parameters can be set using a user-friendly GUI. Users can select which
layers of the original MODIS HDF files they want to process, which
additional quality indicators should be extracted from aggregated MODIS
quality assurance layers and, in the case of surface reflectance products,
which spectral indexes should be computed from the original reflectance
bands. For each output layer, outputs are saved as single-band raster
files corresponding to each available acquisition date. Virtual files
allowing access to the entire time series as a single file are also
created. Command-line execution exploiting a previously saved processing
options file is also possible, allowing users to automatically update time
series related to a MODIS product whenever a new image is available. For
additional documentation refer to the following article: Busetto and
Ranghetti (2016) <doi:10.1016/j.cageo.2016.08.020>.

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
