%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geoflow
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Orchestrate Geospatial (Meta)Data Management Workflows and Manage FAIR Services

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-geometa >= 0.9
BuildRequires:    R-CRAN-geonapi >= 0.8.1
BuildRequires:    R-CRAN-geosapi >= 0.8
BuildRequires:    R-CRAN-ows4R >= 0.5
BuildRequires:    R-CRAN-geonode4R >= 0.1.2
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dotenv 
BuildRequires:    R-CRAN-benchmarkme 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rdflib 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfarrow 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-smoothr 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-geometa >= 0.9
Requires:         R-CRAN-geonapi >= 0.8.1
Requires:         R-CRAN-geosapi >= 0.8
Requires:         R-CRAN-ows4R >= 0.5
Requires:         R-CRAN-geonode4R >= 0.1.2
Requires:         R-CRAN-R6 
Requires:         R-methods 
Requires:         R-CRAN-dotenv 
Requires:         R-CRAN-benchmarkme 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rdflib 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-png 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfarrow 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-smoothr 
Requires:         R-CRAN-terra 

%description
An engine to facilitate the orchestration and execution of metadata-driven
data management workflows, in compliance with 'FAIR' (Findable,
Accessible, Interoperable and Reusable) data management principles. By
means of a pivot metadata model, relying on the 'DublinCore' standard
(<https://dublincore.org/>), a unique source of metadata can be used to
operate multiple and inter-connected data management actions. Users can
also customise their own workflows by creating specific actions but the
library comes with a set of native actions targeting common geographic
information and data management, in particular actions oriented to the
publication on the web of metadata and data resources to provide standard
discovery and access services. At first, default actions of the library
were meant to focus on providing turn-key actions for geospatial
(meta)data: 1) by creating manage geospatial (meta)data complying with
'ISO/TC211' (<https://committee.iso.org/home/tc211>) and 'OGC'
(<https://www.ogc.org/standards/>) geographic information standards (eg
19115/19119/19110/19139) and related best practices (eg. 'INSPIRE'); and
2) by facilitating extraction, reading and publishing of standard
geospatial (meta)data within widely used software that compound a Spatial
Data Infrastructure ('SDI'), including spatial databases (eg. 'PostGIS'),
metadata catalogues (eg. 'GeoNetwork', 'CSW' servers), data servers (eg.
'GeoServer'). The library was then extended to actions for other domains:
1) biodiversity (meta)data standard management including handling of 'EML'
metadata, and their management with 'DataOne' servers, 2) in situ sensors,
remote sensing and model outputs (meta)data standard management by
handling part of 'CF' conventions, 'NetCDF' data format and 'OPeNDAP'
access protocol, and their management with 'Thredds' servers, 3) generic /
domain agnostic (meta)data standard managers ('DublinCore', 'DataCite'),
to facilitate the publication of data within (meta)data repositories such
as 'Zenodo' (<https://zenodo.org>) or DataVerse
(<https://dataverse.org/>). The execution of several actions will then
allow to cross-reference (meta)data resources in each action performed,
offering a way to bind resources between each other (eg. reference
'Zenodo' 'DOI' in 'GeoNetwork'/'GeoServer' metadata, or vice versa
reference 'GeoNetwork'/'GeoServer' links in 'Zenodo' or 'EML' metadata).
The use of standardized configuration files ('JSON' or 'YAML' formats)
allow fully reproducible workflows to facilitate the work of data and
information managers.

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
