%global __brp_check_rpaths %{nil}
%global packname  spocc
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to Species Occurrence Data Sources

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-rbison 
BuildRequires:    R-CRAN-rebird 
BuildRequires:    R-CRAN-rvertnet 
BuildRequires:    R-CRAN-ridigbio 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-wellknown 
Requires:         R-utils 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-rbison 
Requires:         R-CRAN-rebird 
Requires:         R-CRAN-rvertnet 
Requires:         R-CRAN-ridigbio 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-wellknown 

%description
A programmatic interface to many species occurrence data sources,
including Global Biodiversity Information Facility ('GBIF'), 'USGSs'
Biodiversity Information Serving Our Nation ('BISON'), 'iNaturalist',
'eBird', Integrated Digitized 'Biocollections' ('iDigBio'), 'VertNet',
Ocean 'Biogeographic' Information System ('OBIS'), and Atlas of Living
Australia ('ALA'). Includes functionality for retrieving species
occurrence data, and combining those data.

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
