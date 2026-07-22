%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biofetchR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download, Clean, Classify, Enrich and Export Biodiversity Occurrence Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-CoordinateCleaner 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geodata 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mregions2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-CoordinateCleaner 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geodata 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mregions2 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tibble 

%description
Downloads, imports, cleans, classifies, enriches and exports biodiversity
occurrence data, with an emphasis on reproducible Global Biodiversity
Information Facility (GBIF) <https://api.gbif.org/v1/> workflows. The
package supports batch occurrence downloads, taxonomic standardisation,
coordinate cleaning, optional spatial thinning, spatial attribution and
structured export of processed occurrence records and audit outputs.
Terrestrial and freshwater workflows can join records to administrative
units, protected areas, freshwater ecoregions, basins, rivers, lakes,
reservoirs, wetlands and other contextual spatial overlays. Marine
workflows support offshore and coastal records through joins to Marine
Regions <https://www.marineregions.org/> style layers, Exclusive Economic
Zone (EEZ) units, marine ecoregions, Large Marine Ecosystems and
user-supplied marine overlays. The package also supports native-range and
invasive-status evidence workflows using the World Register of Marine
Species (WoRMS) <https://www.marinespecies.org/>, evidence derived from
Standardising and Integrating Alien Species (SInAS)
<https://zenodo.org/records/18220953>, and Global Register of Introduced
and Invasive Species (GRIIS) <https://griis.org/> style species-country
records. These tools are intended for biodiversity, macroecological and
invasion-biology analyses where occurrence records need to be processed
consistently, transparently and reproducibly.

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
