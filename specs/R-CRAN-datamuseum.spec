%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  datamuseum
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial and Taxonomic Data Utilities for Specimen Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
A management tool for specimen data ranging from public museum collections
to private specimen repositories. The main types of data addressed are
spatial (coordinates, longitude and latitude) and taxonomic data (ranking
and nomenclature validity) with some additional options for
user-determined dataset refinement. Combined or individual calls to the
online repositories of the Global Biodiversity Information Facility (GBIF)
via 'rgbif' and the Integrated Taxonomic Information System (ITIS) via
'taxize' enable built-in taxonomic checks.

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
