%global packname  MODIStsp
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          A Tool for Automating Download and Preprocessing of MODIS LandProducts Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5.2
BuildRequires:    R-CRAN-mapview >= 2.3.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-bitops >= 1.0.6
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-xts >= 0.9.7
BuildRequires:    R-CRAN-sf >= 0.9.3
BuildRequires:    R-CRAN-mapedit >= 0.4.1
BuildRequires:    R-CRAN-gdalUtilities 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-raster >= 2.5.2
Requires:         R-CRAN-mapview >= 2.3.0
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-bitops >= 1.0.6
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-xts >= 0.9.7
Requires:         R-CRAN-sf >= 0.9.3
Requires:         R-CRAN-mapedit >= 0.4.1
Requires:         R-CRAN-gdalUtilities 
Requires:         R-CRAN-jsonlite 
Requires:         R-parallel 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-shiny 

%description
Allows automating the creation of time series of rasters derived from
MODIS Satellite Land Products data. It performs several typical
preprocessing steps such as download, mosaicking, reprojection and resize
of data acquired on a specified time period. All processing parameters can
be set using a user-friendly GUI. Users can select which layers of the
original MODIS HDF files they want to process, which additional Quality
Indicators should be extracted from aggregated MODIS Quality Assurance
layers and, in the case of Surface Reflectance products , which Spectral
Indexes should be computed from the original reflectance bands. For each
output layer, outputs are saved as single-band raster files corresponding
to each available acquisition date. Virtual files allowing access to the
entire time series as a single file are also created. Command-line
execution exploiting a previously saved processing options file is also
possible, allowing to automatically update time series related to a MODIS
product whenever a new image is available.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ExtData
%doc %{rlibdir}/%{packname}/Log
%{rlibdir}/%{packname}/testdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
