%global __brp_check_rpaths %{nil}
%global packname  ecochange
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Integrating Ecological Remote Sensing Data to Derive EBV Metrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-gdalUtilities 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-landscapemetrics 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-rasterDT 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgeos 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rgdal 
Requires:         R-parallel 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-gdalUtilities 
Requires:         R-graphics 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-landscapemetrics 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-getPass 
Requires:         R-methods 
Requires:         R-CRAN-rasterVis 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-rasterDT 
Requires:         R-CRAN-data.table 

%description
Essential Biodiversity Variables (EBV) are state variables with dimensions
on time, space, and biological organization that can document biodiversity
change. Freely available remote sensing products (RSP) are downloaded and
integrated with data for national or regional domains to derive metrics
for EBV related to horizontal ecosystem extent, forest fragmentation,
species distribution ranges, among others. To process the spatial data,
the users must provide at least a region of interest (polygon or
geographic administrative unit). Downloadable RSP include Global Surface
Water (Peckel et al., 2016) <doi:10.1038/nature20584>, Forest Change
(Hansen et al., 2013) <doi:10.1126/science.1244693>, and Continuous Tree
Cover data (Sexton et al., 2013) <doi:10.1080/17538947.2013.786146>.

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
